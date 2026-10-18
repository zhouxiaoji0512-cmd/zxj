#!/usr/bin/env python3
"""Add final citation/order and manuscript metadata without changing numeric sheets."""
from pathlib import Path
import json,hashlib,csv
import openpyxl,fitz
from openpyxl.styles import Font,PatternFill
R=Path(__file__).resolve().parents[1];REPO=R.parent
book=openpyxl.load_workbook(R/'数据总表.xlsx')
for name in ['全稿引文编号','全稿说明']:
 if name in book:del book[name]
ws=book.create_sheet('全稿引文编号');fields=['number','id','title','year','journal','volume','pages','article_number','doi','source_file','formatted_entry'];ws.append(fields)
for row in json.loads((R/'data/citation_map.json').read_text())['references']:ws.append([row.get(k) for k in fields])
ws=book.create_sheet('全稿说明');ws.append(['项目','内容'])
for row in [('状态','完整初稿及最终交付文件；运行参数和成键候选仍有待核实项目'),('正文汉字',json.loads((R/'data/manuscript_counts.json').read_text())['body_cjk_characters']),('含正文图表说明汉字',json.loads((R/'data/manuscript_counts.json').read_text())['main_with_figures_tables_cjk_characters']),('单位与定义','未知距离/AIM/CT/NOCV单位不默认填充；Eb-Eint仅表列差量'),('来源','所有定量原值保留，正文D01-D17对应2733条逐值来源'),('引文','全稿引文编号按正文首次出现顺序；原始参考文献表保留其来源状态')]:ws.append(row)
for ws in book:
 ws.freeze_panes='A2'
 if ws.title in ['全稿引文编号','全稿说明']:
  ws.auto_filter.ref=ws.dimensions
  for c in ws[1]:c.font=Font(bold=True,color='FFFFFF');c.fill=PatternFill('solid',fgColor='305A72')
  for col in ws.columns:ws.column_dimensions[col[0].column_letter].width=40
book.save(R/'数据总表.xlsx')
refs=json.loads((R/'audit/references.json').read_text());uses={row['source_file']:row['id']+'；'+row['title'] for row in refs['references']}
rows=[]
for p in sorted(REPO.iterdir()):
 if not p.is_file():continue
 if p.suffix not in ['.pdf','.docx','.xlsx','.md']:continue
 item={'文件':p.name,'字节数':p.stat().st_size,'SHA256':hashlib.sha256(p.read_bytes()).hexdigest(),'用途':uses.get(p.name,'原始大纲/数据，或此前已读但本轮不纳入正式正文引文的资料'),'读取说明':'先前阶段建立读取记录；本轮按写作与审校需要回查，不声称逐页重读全部实验谱图'}
 if p.suffix=='.pdf':
  with fitz.open(p) as d:item['PDF页数']=len(d)
 rows.append(item)
with (R/'原始资料清单.csv').open('w',encoding='utf-8-sig',newline='') as f:
 keys=['文件','字节数','SHA256','用途','读取说明','PDF页数'];w=csv.DictWriter(f,fieldnames=keys,lineterminator='\n');w.writeheader();w.writerows(rows)
(R/'data/original_inventory.json').write_text(json.dumps(rows,ensure_ascii=False,indent=2))
print('Summary workbook:',len(book.sheetnames),'sheets; original inventory:',len(rows),'files.')
