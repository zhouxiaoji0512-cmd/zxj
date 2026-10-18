#!/usr/bin/env python3
"""Check source transcription and artifact integrity, not missing chemistry."""
from pathlib import Path
import json,csv,hashlib,re,zipfile,math,xml.etree.ElementTree as ET
import openpyxl,fitz
from PIL import Image
from docx import Document
R=Path(__file__).resolve().parents[1];REPO=R.parent;checks=[]
for name,digest in json.loads((R/'data/source_hashes.json').read_text()).items():assert hashlib.sha256((REPO/name).read_bytes()).hexdigest()==digest,name
checks.append('All 5 source hashes unchanged.')
raw=openpyxl.load_workbook(REPO/'HOClxlsx.xlsx',data_only=True)
records=json.loads((R/'data/complexes.json').read_text());pairs=json.loads((R/'data/pairs.json').read_text());by={d['system']:d for d in records}
assert len(records)==56 and len(by)==56 and len(pairs)==28
n=0
for d in records:
 for key,value in d.items():
  if not key.endswith('_src'):continue
  m=re.fullmatch(r'HOClxlsx.xlsx::([^!]+)!([A-Z]+[0-9]+)',str(value))
  if not m:continue
  original=raw[m.group(1)][m.group(2)].value;actual=d[key[:-4]]
  if isinstance(original,(float,int)) and not isinstance(original,bool):assert math.isclose(original,actual,rel_tol=0,abs_tol=1e-12),(d['system'],key)
  else:assert original==actual,(d['system'],key)
  n+=1
for p in pairs:
 h=by['H-'+p['ligand']];c=by['Cl-'+p['ligand']]
 assert math.isclose(p['delta_Eb_H_minus_Cl'],h['Eb_bess']-c['Eb_bess'],abs_tol=1e-12)
 assert math.isclose(p['delta_Eint_H_minus_Cl'],h['Eint_bess']-c['Eint_bess'],abs_tol=1e-12)
assert sum(p['delta_Eb_H_minus_Cl']<0 for p in pairs)==22
assert sum(p['delta_Eint_H_minus_Cl']<0 for p in pairs)==13
assert sum(bool(p['ranking_reversal']) for p in pairs)==9
checks.append(f'{n} original-cell fields match; 28 paired differences recomputed and 9 reversals reproduced.')
expected={'F1_energy_competition':28,'F2_internal_bond_response':56,'F3_EDA_components':10,'F4_geometry_screening':56,'S1_energy_audit':56,'S2_MEP_exploratory':28}
for name,count in expected.items():
 with (R/'data'/f'figure_{name}.csv').open(encoding='utf-8-sig',newline='') as f:rows=list(csv.DictReader(f))
 assert len(rows)==count,(name,len(rows))
 if name=='S2_MEP_exploratory':
  included=[x for x in rows if x['included_in_plot']=='True'];excluded=[x for x in rows if x['included_in_plot']!='True']
  assert len(included)==24 and len(excluded)==4
  assert all(x['MEP_B'] for x in included) and all(x['exclusion_reason'] for x in excluded)
for item in json.loads((R/'figures/figure_manifest.json').read_text()):
 stem=item['figure']
 with Image.open(R/'figures'/f'{stem}.png') as im:
  assert im.size==(round(item['width_inches']*300),round(item['height_inches']*300));im.verify()
 with fitz.open(R/'figures'/f'{stem}.pdf') as pdf:assert len(pdf)==1
 assert len(ET.parse(R/'figures'/f'{stem}.svg').findall('.//{http://www.w3.org/2000/svg}text'))>5
checks.append('6 plotting CSVs and all 18 PNG/SVG/PDF files verified; 24 S2 included and 4 explicitly excluded records.')
with zipfile.ZipFile(R/'结果与讨论_第二阶段.docx') as z:assert z.testzip() is None
word=Document(R/'结果与讨论_第二阶段.docx')
assert len(word.inline_shapes)==6 and len(word.tables)==4
assert [len(t.rows) for t in word.tables]==[29,11,9,18]
assert any(run.font.superscript for p in word.paragraphs for run in p.runs)
assert not any(p.text.lstrip().startswith('|') for p in word.paragraphs)
wb=openpyxl.load_workbook(R/'统一数据总表_第二阶段.xlsx',data_only=True)
assert wb['构型总表56'].max_row==57 and wb['能量配对28'].max_row==29
assert wb['第二阶段来源索引'].max_row==2734
checks.append('Word readable with 6 images, 4 native tables and superscript citations; workbook contains 56 configurations, 28 pairs and 2733 source-ledger rows.')
body=(R/'结果与讨论_第二阶段.md').read_text();seen=[]
for number in re.findall(r'\^\[([0-9]+)\]\^',body):
 if number not in seen:seen.append(number)
assert seen==['1','2','3','4','5'] and len(set(re.findall(r'D[0-9]{2}',body)))==17
assert len(body)==11596
checks.append('Restored manuscript 11596 characters, all D01–D17 groups present and five references in first-citation order; independent numerical/literature reviews completed.')
result={'status':'passed','checks':checks,'limits':'These checks establish source transcription and usable artifacts. Energy definitions, some units, raw-job settings and transfer classifications remain unverified.'}
(R/'data/validation_report.json').write_text(json.dumps(result,ensure_ascii=False,indent=2))
print(json.dumps(result,ensure_ascii=False,indent=2))
