#!/usr/bin/env python3
"""Assemble complete draft and supplements from frozen evidence and reviewed components."""
from pathlib import Path
import json,re,csv,ast,hashlib
from docx import Document
R=Path(__file__).resolve().parents[1];REPO=R.parent
parts=['00_frontmatter.md','01_introduction.md','02_methods.md','03_05_results.md','06_conclusions.md']
chunks=[]
for name in parts:
 text=(R/'components'/name).read_text()
 # Normalize numbering while preserving the user's six-chapter scientific order.
 text=re.sub(r'^#{1,3} ([1-6]) (.+)$',r'## \1 \2',text,flags=re.M)
 text=re.sub(r'^#{1,3} ([1-6]\.[0-9]+) (.+)$',r'### \1 \2',text,flags=re.M)
 chunks.append(text.strip())
source='\n\n'.join(chunks)+'\n'
source=source.replace('NCH形成的复合物','HCN（原文记为NCH）形成的复合物')
source=source.replace('原表BD*','原表BD\\*').replace('BD*','BD\\*').replace('σ*','σ\\*')
# Ordered citations are resolved only after the complete text is assembled.
bib=json.loads((R/'audit/references.json').read_text());lookup={x['id']:x for x in bib['references']}
order=list(dict.fromkeys(re.findall(r'\{\{(R[0-9]{2})\}\}',source)))
assert set(order)<=set(lookup)
num={key:i+1 for i,key in enumerate(order)}
def cite(m):
 codes=re.findall(r'R[0-9]{2}',m.group())
 return '^['+','.join(str(n) for n in sorted({num[key] for key in codes}))+']^'
body=re.sub(r'(?:\{\{R[0-9]{2}\}\})+',cite,source)
assert '{{R' not in body
entries=[]
for key in order:
 item=lookup[key].copy();gbt=item['gbt7714']
 if key=='R04':gbt=gbt.replace('2014. DOI:','2014[2026-10-18]. DOI:')
 if key=='R11':gbt=gbt.replace('2021, 86. DOI:','2021, 86[2026-10-18]. DOI:')
 item['number']=num[key];item['formatted_entry']=f'[{num[key]}] '+gbt;entries.append(item)
(R/'data/citation_map.json').write_text(json.dumps({'order':order,'mapping':num,'references':entries},ensure_ascii=False,indent=2))
refs='## 参考文献\n\n'+'\n\n'.join(e['formatted_entry'] for e in entries)+'\n'
(R/'参考文献.md').write_text(refs)
with (R/'参考文献.csv').open('w',encoding='utf-8-sig',newline='') as f:
 fields=['number','id','authors','title','year','journal','volume','pages','article_number','doi','source_file','formatted_entry'];w=csv.DictWriter(f,fieldnames=fields,lineterminator='\n');w.writeheader()
 for item in entries:
  row={k:item.get(k) for k in fields}
  if isinstance(row['authors'],list):row['authors']='; '.join(row['authors'])
  w.writerow(row)
# Preserve previously checked captions, without importing/running the stage-two builder.
cache=R/'data/figure_captions.json'
if cache.exists():caption=json.loads(cache.read_text())
else:
 module=ast.parse((REPO/'report2/scripts/build_manuscript.py').read_text())
 caption=next(ast.literal_eval(n.value) for n in module.body if isinstance(n,ast.Assign) and any(isinstance(t,ast.Name) and t.id=='caption' for t in n.targets))
(R/'data/figure_captions.json').write_text(json.dumps(caption,ensure_ascii=False,indent=2))
(R/'图注.md').write_text('# 论文图注\n\n'+'\n\n'.join(t+'\n\n'+c for t,c in caption.values())+'\n')
# Result tables come from the previously checked native tables; raw numeric data remain in JSON/Excel.
cache=R/'data/result_tables.json'
if cache.exists():tables=json.loads(cache.read_text())
else:
 old=Document(REPO/'report2/结果与讨论_第二阶段.docx')
 tables={name:[[cell.text for cell in row.cells] for row in table.rows] for name,table in zip(['表3-1','表4-3','表5-1'],old.tables[:3])}
(R/'data/result_tables.json').write_text(json.dumps(tables,ensure_ascii=False,indent=2))
notes={
'表3-1':'能量单位kcal/mol，差量统一H减Cl。来源：HOClxlsx.xlsx的bess列B/C/F/G及编号对照；逐值见D04/D05。参考态、BSSE和ZPE待核实。',
'表4-3':'保留EDA全部原列。仅ES列头明示kcal/mol，其余同单位暂作审阅图假设；不把ECORR改称纯色散。来源D12。',
'表5-1':'几何和拓扑字段的单位及BCP原子对待核实，E(2)为kcal/mol；缺失WBI不填0。来源D03/D09/D10/D14/D15。'}
table_titles={'表3-1':'表1 两端能量及配对差量','表4-3':'表2 代表构型的EDA五分项与总量','表5-1':'表3 强相互作用候选与参照构型的联合证据'}
def mdtable(name):
 rows=tables[name]
 return '\n\n'+table_titles[name]+'\n\n| '+' | '.join(rows[0])+' |\n| '+' | '.join('---' for _ in rows[0])+' |\n'+'\n'.join('| '+' | '.join(row)+' |' for row in rows[1:])+'\n\n'+notes[name]+'\n\n'
def fig(stem):
 title,cap=caption[stem]
 return f'\n\n![](figures/{stem}.png){{width=100%}}\n\n{title}。{cap}\n\n'
inserts={'### 3.3':fig('F2_bond_response'),'### 3.4':fig('F1_energy_competition')+mdtable('表3-1'),'### 4.4':fig('F3_eda_components')+mdtable('表4-3'),'### 5.2':fig('F4_geometry_candidates')+mdtable('表5-1')}
combined=[]
for line in body.splitlines():
 for key,value in inserts.items():
  if line.startswith(key):combined.append(value)
 combined.append(line)
main='\n'.join(combined)+'\n\n'+refs
(R/'论文_正文.md').write_text(body+'\n'+refs)
(R/'论文_图文整合.md').write_text(main)
# Supplement keeps full traceability and unresolved requirements outside the main narrative.
ledger=(R/'data/source_ledger_summary.md').read_text().replace('## 附录A 定量陈述来源表','## S1 数据来源与核查范围')
limits=(R/'data/requirements_source.md').read_text().replace('# 第二阶段待核实与最小补充清单','# 全稿待核实与最小补充清单')
sup='# 补充材料与待核实事项\n\n## 摘要及全文统计的追溯说明\n\n摘要的28/56来源D01，22/6、13/15及9反转来源D04/D05；候选与EDA符号来源D11/D14/D15。正文沿用[D01]—[D17]，逐值来源见data/数据来源索引.csv（2733条）。所有原值与bess保留，核查只证明转录和算术一致，不代替原始作业验证。\n\n'+ledger+'\n\n## S2 统计口径与证据限制\n\nH/Cl标签表示原表取向，统计分母固定为28对或56条构型。CT的26/20表示28对中26对Cl端表值更大，其中20对仍为H端Eb较低。LP/BD计数为原表主供体类别，BCP身份、单位和跨分析几何仍待原始输出确认。近零差没有方法误差棒，不推算平衡丰度或速率。\n\n## S3 补充图\n\n'+fig('S1_energy_audit')+fig('S2_mep_competition')+'\n\n## S4 最小补充清单\n\n'+re.sub(r'^# .+\n','',limits,count=1)+'\n\n## S5 书目与资料范围\n\n11项正式或可用DOI定位的文献已按上传PDF核读。R04和R11上传件缺最终页码，按[J/OL]及DOI著录，未编页码；R12编辑占位手稿及R13/R14仅有SI的父文献记录不作已核实正文引用。本次未声称穷尽全部国内外研究或进行新的在线书目核验。\n'
(R/'补充材料.md').write_text(sup)
(R/'待核实事项.md').write_text(limits+'\n\n## 全稿待补充的信息\n\n作者与单位尚未提供。原始运行参数、完整组成及能量定义仍为待核实，不得因全稿已排版而删除标记。最终文件是完整初稿及审校材料，不是已经补齐原始计算的投稿定稿。\n')
outline=[
['第一章1.1—1.6','全文第1章','保留基础、国内外进展、HOCl现状、研究问题；不宣称首次。'],
['第二章2.1—2.8','全文第2章','保留实际证据范围；计算运行条件以待核实字段呈现。'],
['第三章3.1—3.4','全文第3章','保留位点、结构、能量竞争及几何—能量关系，补充名称系列。'],
['第四章4.1—4.5','全文第4章','保留NBO/AIM/EDA/NOCV与综合讨论，未提供通道不绘虚构密度图。'],
['第五章5.1—5.4','全文第5章','原标题成键机制改为候选证据分析，并使用“强相互作用候选的结构重排与电子证据”，因为缺少路径和充分的新旧键证据。'],
['第六章6.1—6.4','全文第6章','对应竞争、电子机制、强作用候选与局限，不把待验假设写成结果。']]
(R/'大纲对应关系.md').write_text('# 原大纲与完整初稿对应\n\n|原大纲|全稿位置|理由/处理|\n|---|---|---|\n'+'\n'.join('| '+' | '.join(row)+' |' for row in outline)+'\n')
counts={'body_cjk_characters':len(re.findall(r'[\u4e00-\u9fff]',body)),'body_all_characters':len(body),'main_with_figures_tables_cjk_characters':len(re.findall(r'[\u4e00-\u9fff]',main.split('## 参考文献')[0])),'references':len(entries),'main_figures':4,'supplementary_figures':2,'native_result_tables':3,'reference_order':order}
(R/'data/manuscript_counts.json').write_text(json.dumps(counts,ensure_ascii=False,indent=2))
print(json.dumps(counts,ensure_ascii=False,indent=2))
