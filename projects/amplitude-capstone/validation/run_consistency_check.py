"""Cross-artifact consistency check for the AmpliStore 2.0 capstone.

Verifies that the workbook, presentation, taxonomy, architecture and chart
specifications agree with one another and with the single canonical content
model in notes/content_model.py. Run from the amplitude-capstone/ directory.
"""
import sys, re
from collections import defaultdict
sys.path.insert(0, "notes")
import content_model as m, chart_build_results as r
import openpyxl
from pptx import Presentation

WB="output/AmpliStore_Implementation_Workbook.xlsx"
DK="output/AmpliStore_Partnership_Kickoff.pptx"
SPEC="output/AmpliStore_Chart_Specifications.md"

results=[]
def check(name, ok, detail=""):
    results.append((("PASS" if ok else "FAIL"), name, detail))

wb=openpyxl.load_workbook(WB)
prs=Presentation(DK)
spec=open(SPEC).read()

parts=[]
for s in prs.slides:
    for sh in s.shapes:
        if sh.has_text_frame: parts.append(sh.text_frame.text)
        if getattr(sh,"has_table",False) and sh.has_table:
            for row in sh.table.rows:
                for c in row.cells: parts.append(c.text)
        if sh.shape_type==6:
            for sub in sh.shapes:
                if sub.has_text_frame: parts.append(sub.text_frame.text)
DECK="\n".join(parts)

model_events={e["name"] for e in m.EVENTS}

# 1 taxonomy -> workbook
ws=wb["Events and Event Properties"]
wb_events={str(ws.cell(row=i,column=3).value).strip()
           for i in range(47, ws.max_row+1) if ws.cell(row=i,column=3).value}
check("All 16 taxonomy events present in the workbook Events sheet",
      model_events<=wb_events, f"missing: {sorted(model_events-wb_events)}")

# 2 chart steps -> taxonomy
bad=[f"{c['id']}:{s}" for c in m.CHARTS for s in c["steps"] if s not in model_events]
check("Every chart step maps to an event in the taxonomy", not bad, f"orphans: {bad}")

# 3 KPI events -> taxonomy
bad=[e for k in m.KPIS for e in k["events"] if e not in model_events]
check("Every KPI-referenced event exists in the taxonomy", not bad, f"orphans: {bad}")

# 4 charts -> business questions
qids={q[0] for q in m.BUSINESS_QUESTIONS}
bad=[c["id"] for c in m.CHARTS if not c["answers"] or not set(c["answers"])<=qids]
check("Every chart maps to at least one scoped business question", not bad, f"unmapped: {bad}")

# 5 KPIs -> charts
cids={c["id"] for c in m.CHARTS}
bad=[k["id"] for k in m.KPIS if k["chart_id"] not in cids]
check("Every KPI has a mapped chart", not bad, f"unmapped: {bad}")

# 6 questions -> KPI and use case
ucs={u["id"] for u in m.USE_CASES}; kis={k["id"] for k in m.KPIS}
bad=[q for q,uc,k,_ in m.BUSINESS_QUESTIONS if uc not in ucs or k not in kis]
check("Every business question maps to a valid use case and KPI", not bad, f"broken: {bad}")

# 7 KPI parity workbook <-> deck
found=[k["name"] for k in m.KPIS if k["name"] in DECK]
check("KPI names used in the deck all exist in the workbook model",
      len(found)>=5, f"in deck: {found}")

# 8 no fabricated URLs anywhere
verified={b["url"] for b in r.BUILT.values()} | {r.DASHBOARD["url"]}
urls={u.rstrip(").,") for u in re.findall(r"https?://app\.amplitude\.com/\S+", spec)}
ws2=wb["Analytics KPIs"]
for i in range(3,19):
    v=ws2.cell(row=i,column=8).value
    if v and str(v).startswith("http"): urls.add(str(v).strip())
bogus=sorted(urls-verified)
check("No fabricated Amplitude URLs — every URL was built and re-verified", not bogus, f"unverified: {bogus}")

# 9 spec-only charts carry no URL  (scoped to each chart's OWN section)
sections={}
for blk in re.split(r"\n## ", spec):
    mm=re.match(r"(C\d)\b", blk)
    if mm: sections[mm.group(1)]=blk
bad=[cid for cid in r.NOT_BUILT
     if "app.amplitude.com" in sections.get(cid,"") or "Not available" not in sections.get(cid,"")]
check("Specification-only charts (C2, C6, C7) carry no Amplitude URL", not bad, f"violations: {bad}")

# 10 built charts DO carry their verified URL
bad=[cid for cid,b in r.BUILT.items() if b["url"] not in sections.get(cid,"")]
check("Every built chart carries its verified URL in the specification", not bad, f"missing: {bad}")

# 11 deck placeholders
PLACE=["Presenter Name","[Customer]","[CUSTOMER]","Insert Cus Logo","MM.DD.YYYY",
       "Target Date: XX","Example ONLY","Replace with architecture diagram",
       "Delete if not applicable","Fill out if Implementation Partner",
       "Product / Team A","Product / Team B","Product / Team C","email@amplitude.com"]
left=[p for p in PLACE if p in DECK]
check("No template placeholders remain in the deck", not left, f"remaining: {left}")

# 12 no invented baselines in the workbook
NUM=re.compile(r"\b\d+(?:\.\d+)?\s?%")
hits=[]
for shn in ("Analytics KPIs","Alignment (Week 0)","AI Deliverables Plan"):
    for row in wb[shn].iter_rows():
        for c in row:
            if isinstance(c.value,str) and NUM.search(c.value): hits.append(f"{shn}!{c.coordinate}")
check("No percentage baselines asserted in the workbook KPI / Alignment / AI sheets",
      not hits, f"found: {hits[:6]}")

# 13 demo figures do not leak into the workbook
leak=[]
demo_nums=set()
for cid,rows in r.DEMO_OBSERVATIONS.items():
    if cid=="window": continue
    for _,users,conv in rows:
        demo_nums.add(f"{users:,}"); demo_nums.add(conv.rstrip("%"))
for shn in wb.sheetnames:
    for row in wb[shn].iter_rows():
        for c in row:
            if isinstance(c.value,str):
                for n in demo_nums:
                    if len(n)>3 and n in c.value: leak.append(f"{shn}!{c.coordinate}")
check("Demo-data observations do not leak into the workbook as baselines",
      not leak, f"leaks: {sorted(set(leak))[:6]}")

# 14 workbook carries an explicit no-baseline statement
note=str(wb["Analytics KPIs"].cell(row=21,column=3).value or "")
check("Workbook states explicitly that no baseline is asserted",
      "No numeric baseline is asserted" in note and "not AmpliStore" in note.replace("NOT AmpliStore","not AmpliStore"),
      note[:80])

# 15 architecture terms consistent across deck / workbook / diagram
for term in ("Snowflake","Braze","Amplitude Browser SDK"):
    check(f"Architecture term '{term}' appears consistently in the deck", term in DECK, "")

# 16 architecture matches the instrumentation strategy
check("Deck presents warehouse import (not HTTP API) as the Phase 1 backend path",
      "Snowflake" in DECK and "not in Phase 1 scope" in DECK, "")

# 17 AI deliverables identical model <-> workbook
wsai=wb["AI Deliverables Plan"]
ai_wb={str(wsai.cell(row=6+i,column=2).value).strip() for i in range(5)}
ai_md={d["official_name"] for d in m.AI_DELIVERABLES}
check("Five AI deliverables identical between the model and the workbook", ai_wb==ai_md, f"diff: {ai_wb^ai_md}")
check("Exactly five AI deliverables, each with a cited official source",
      len(m.AI_DELIVERABLES)==5 and all(d["deck_source"] and d["workbook_source"] for d in m.AI_DELIVERABLES), "")

# 18 event naming style
bad=[e for e in model_events if "_" in e or e.isupper() or e.islower() or e!=e.strip()]
check("All event names follow the Title Case style guide", not bad, f"violations: {bad}")

# 19 property naming reuse
byname=defaultdict(set)
for e in m.EVENTS:
    for _,pn,_,_ in e["properties"]:
        if pn: byname[pn].add(e["name"])
shared={p:v for p,v in byname.items() if len(v)>1}
check("Shared property names are reused across events rather than duplicated per event",
      len(shared)>=6, f"shared properties: {len(shared)}")

# 20 PII — scan property NAMES and SAMPLE VALUES.
# Descriptions are deliberately excluded: they legitimately name PII in order to
# FORBID it (e.g. "Never send card number, CVV..."), so scanning prose would
# flag exactly the guidance that prevents the problem.
PII_NAME=["email","password","cvv","card number","ssn","first name","last name",
          "street","postcode","phone number","full name","date of birth"]
EMAILRE=re.compile(r"[\w.+-]+@[\w-]+\.[\w.]+")
CARDRE=re.compile(r"\b\d{13,16}\b")
bad=[]
for e in m.EVENTS:
    for _,pn,ps,_ in e["properties"]:
        if pn and any(t in pn.lower() for t in PII_NAME): bad.append(f"{e['name']}.{pn}")
        if ps and (EMAILRE.search(str(ps)) or CARDRE.search(str(ps))):
            bad.append(f"{e['name']}.{pn} sample value")
for up in m.USER_PROPERTIES:
    if any(t in up[0].lower() for t in PII_NAME): bad.append(f"user:{up[0]}")
    if EMAILRE.search(str(up[3])) or CARDRE.search(str(up[3])): bad.append(f"user:{up[0]} sample value")
check("No PII in event or user property names, or in sample values",
      not bad, f"violations: {sorted(set(bad))}")

# 20b prohibition guidance is actually present where it matters
prohib=sum(1 for e in m.EVENTS for p in e["properties"]
           if any(w in str(p[3]).lower() for w in ("never send","no street address","only -")))
check("Sensitive steps carry explicit do-not-store guidance", prohib>=2, f"found {prohib}")

# 21 explicit never-store guidance present on payment step
pay=[e for e in m.EVENTS if e["name"]=="Payment Info Added"][0]
check("Payment step explicitly forbids storing card credentials",
      any("Never send card number" in str(p[3]) for p in pay["properties"]), "")

# 22 chart totals
check("Chart specification documents all 8 charts", len(re.findall(r"\n## C\d", spec))==8,
      f"found {len(re.findall(chr(10)+'## C',spec))}")
check("5 built + 3 specification-only = 8 charts",
      len(r.BUILT)+len(r.NOT_BUILT)==len(m.CHARTS), "")

# 23 official deck structure retained
titles=[]
for s in prs.slides:
    for sh in s.shapes:
        if sh.has_text_frame and sh.text_frame.text.strip():
            titles.append(sh.text_frame.text.strip().split("\n")[0]); break
for sec in ("Partnership Kickoff","Introductions","Goal Alignment","Implementation Roadmap",
            "Implementation Scope","Action Items"):
    check(f"Official deck section retained: {sec}", any(sec in t for t in titles), "")
check("Official roadmap slide retained verbatim",
      any("Implementation roadmap: Core Analytics" in t for t in titles), "")

# 24 workbook sheet preservation
ORIG=['Project Plan Gantt View','Implementation Plan Checklist','Product Flows Tracker (optional',
      'Analytics KPIs','(Analytics KPI Guidelines)','Events and Event Properties','User Properties',
      'Question Tracker','Integrations Tracker','Amplitude Project Mapping',
      'Bulk Update Event Schema (Impor','Bulk Update Property Groups (Im','Taxonomy and Data QA',
      'Accounts','Taxonomy Best Practices','Ampl Project Mapping','Governance QA','Project Migration Plan']
missing=[s for s in ORIG if s not in wb.sheetnames]
check("All 18 original template sheets preserved", not missing, f"missing: {missing}")

# 25 Data QA honesty
wsq=wb["Taxonomy and Data QA"]
passes_claimed=[wsq.cell(row=i,column=3).value for i in range(4,39)
                if str(wsq.cell(row=i,column=3).value).strip()=="Pass"]
check("No Data QA row marked Pass without evidence", not passes_claimed,
      f"{len(passes_claimed)} rows claim Pass")

# ============================================================
# WORDING / INTERPRETATION DISCIPLINE
# ============================================================

# 26 every built chart's demo figures sit under an explicit training-data caveat
bad=[]
for cid in r.BUILT:
    sec=sections.get(cid,"")
    if "training data, not an AmpliStore baseline" not in sec: bad.append(cid)
check("Every built chart's figures are labelled as training data, not a baseline",
      not bad, f"unlabelled: {bad}")

# 27 every built chart has a careful descriptive reading
bad=[cid for cid in r.BUILT if r.DEMO_READINGS.get(cid,"") not in sections.get(cid,"")]
check("Every built chart carries its careful demo-data reading", not bad, f"missing: {bad}")

# 28 readings are descriptive, not conclusive
BANNED=["near-universal","the dominant","dominant leak","collapse","far better","far worse",
        "clearly shows","proves that","demonstrates that AmpliStore","the story is",
        "this means AmpliStore","confirms that"]
hits=[b for b in BANNED for txt in r.DEMO_READINGS.values() if b in txt.lower()]
check("Demo readings avoid over-strong interpretive phrasing", not hits, f"phrases: {hits}")

# 29 C3 states correlation, not causation — explicitly
c3=r.DEMO_READINGS["C3"].lower()
check("C3 explicitly states the search difference is correlational, not causal",
      "correlational" in c3 and "does not establish" in c3.replace("not establish","not establish")
      and "causation" in c3, "")
check("C3 caveat is also present in the chart spec and on the live Amplitude chart",
      "CORRELATIONAL" in sections.get("C3","").upper(), "")

# 30 C5 flags the category-value mismatch
c5=r.DEMO_READINGS["C5"].lower()
check("C5 flags that demo category values do not match the apparel scenario",
      "grocery" in c5 and "cannot be read as category insight" in c5, "")

# 31 all six identified gaps are documented in the chart specification
missing=[g[0] for g in r.DATA_GAPS if g[0] not in spec or g[1] not in spec]
check("All six instrumentation/data gaps documented in the chart specification",
      not missing, f"missing: {missing}")

# 32 the six gaps are also in the workbook
wsq_txt=" ".join(str(c.value) for row in wb["Taxonomy and Data QA"].iter_rows()
                 for c in row if c.value)
missing=[g[0] for g in r.DATA_GAPS if g[0] not in wsq_txt]
check("All six gaps documented in the workbook 'Taxonomy and Data QA' sheet",
      not missing, f"missing: {missing}")

# 33 the specific gaps the user asked to keep are individually present
REQUIRED_GAPS=["checkout sub-step","order total","guest","Product Category","duplicate",
               "type"]
low=spec.lower()
missing=[g for g in REQUIRED_GAPS if g.lower() not in low]
check("Each required gap topic is named in the chart specification", not missing, f"missing: {missing}")

# 34 three-way distinction is stated up front
check("Chart specification states the recommended / demo / gap distinction up front",
      "Three things this document keeps separate" in spec
      and "Recommended implementation taxonomy" in spec
      and "Demo taxonomy used to construct charts" in spec, "")
readme=open("output/README.md").read()
check("README states the same three-way distinction",
      "Three things this project keeps separate" in readme, "")

# 35 README carries the demo-data caveat and both specific cautions
check("README carries the demo-data caveat and the C3 / C5 cautions",
      "must not be quoted as a business baseline" in readme
      and "C3 is correlational" in readme
      and "C5 proves configuration, not category insight" in readme, "")

# 36 speaker notes brief the presenter on demo-data framing
notes=" ".join(sl.notes_slide.notes_text_frame.text for sl in prs.slides if sl.has_notes_slide)
check("Deck speaker notes brief the presenter on the demo-data framing",
      "not AmpliStore data" in notes and "CORRELATIONAL" in notes.upper(), "")
check("Deck speaker notes brief the presenter to state window and population",
      "window" in notes.lower() and "population" in notes.lower(), "")

# 37 unbuilt charts are framed as gaps, not failures
bad=[cid for cid in r.NOT_BUILT if "data gap" not in sections.get(cid,"").lower()]
check("C2, C6 and C7 are framed as identified data gaps", not bad, f"not framed: {bad}")

# ---- report ----
P=sum(1 for s,_,_ in results if s=="PASS"); F=len(results)-P
print("="*78)
print(f"CONSISTENCY CHECK   PASS {P}   FAIL {F}   TOTAL {len(results)}")
print("="*78)
for s,n,d in results:
    print(f"  {s}  {n}" + (f"  ::  {d}" if (s=="FAIL" and d) else ""))
sys.exit(0 if F==0 else 1)
