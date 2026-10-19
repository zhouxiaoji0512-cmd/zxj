#!/usr/bin/env python3
"""Apply the documented editorial changes to a copy of the audited baseline."""
from pathlib import Path
import json

ROOT = Path(__file__).resolve().parents[1]
changes = []

def replace(relative, old, new, reason):
    path = ROOT / relative
    text = path.read_text()
    if old in text:
        assert text.count(old) == 1, (relative, old)
        path.write_text(text.replace(old, new))
    else:
        assert new in text, (relative, old)
    changes.append(dict(file=relative, before=old, after=new, reason=reason))

f = 'components/00_frontmatter.md'
replace(f, '完整EDA展示了吸引项与排斥项的显著抵消，并有三个H端构型的ECORR为正，不能将该列未经定义改称纯色散。',
        'EDA各分项表现出吸引与排斥的显著抵消，三个H端构型的ECORR为正，其物理解释仍依赖具体分解定义。',
        '摘要聚焦结果及其解释条件，保留ECORR正值与定义限制。')

f = 'components/01_introduction.md'
replace(f, '典型氢键可表示为D—H···A，其中A向与氢原子相联系的受体轨道提供电子密度；',
        '典型氢键可表示为D—H···A；在供受体轨道图像中，受体A的占据轨道可与D—H反键轨道发生相互作用。',
        '明确轨道解释中的供体与受体，避免用轨道描述代替完整成键定义。')

f = 'components/03_05_results.md'
replace(f,
        '依据编号对照表，当前数据由28个母体标签及其H端、Cl端记录构成，共56条构型记录。结构、能量、NBO、AIM、EDA与NOCV各表按体系名称连接后，均覆盖相同的56个名称，未发现命名重复、缺项或额外构型。这里的H端与Cl端沿用原数据的取向标签，不预先等同于普通氢键和普通卤键。完整配体组成、中心碳原子编号及优化后连接方式仍为【待补充】，因而名称对应不能替代分子结构对应。尤其“CSNHCme不在研究范围内”与“SCNHCme被保留”的命名关系，应在结构表中明确，而不能自行将二者合并或增补。[D01]',
        '按2.2节的名称对应规则，28个母体标签形成56条H端和Cl端记录，所涉分析表的名称覆盖一致。[D01] H端与Cl端沿用原数据的取向标签，不预先限定成键类型；以下比较限于名称层面，完整结构对应仍待坐标确认。完整配体组成、中心碳原子编号及优化后连接方式为【待补充】，命名歧义见2.2节。',
        '方法保留完整核查规则，结果开头集中说明比较对象与结构身份限制。')
replace(f,
        '几何数据采用表列游离HOCl的O—H=0.97950、O—Cl=1.71675为差量基准。56条构型的Δr(O—H)和Δr(O—Cl)均可由相应内部键长减去该基准复算，公式缓存与独立复算一致。图3-4以H端Δr(O—H)及Cl端Δr(O—Cl)分别展示两类取向的内部键响应，不将不同原子对的距离直接解释为同一成键尺度。当前单位和基准理论水平仍为【待核实】，正文和图轴保留“原表距离单位未注明”的限定。[D03]',
        '以表列游离HOCl的O—H=0.97950、O—Cl=1.71675为差量基准，图3-4分别比较H端Δr(O—H)与Cl端Δr(O—Cl)，考察两类取向下被扰动内部键的响应。不同原子对的距离不直接作为同一成键尺度；距离单位和单体基准的理论水平仍为【待核实】。[D03]',
        '将缓存复算过程留在方法，保留基准数值及未知单位。')
replace(f, '这里描述的是C—H距离在当前H端样本中较短，以及O—H相对已列单体基准伸长，并没有同一体系反应前C—H键可供讨论其“缩短量”。',
        '上述比较中，C—H描述复合物中的接触距离，O—H伸长量以表列游离HOCl为参照，两者的参照方式不同。',
        '以正面定义解释距离与变化量的不同参照。')
replace(f, '图5-1采用C···H与O—H、C···Cl与O—Cl的成对几何散点进行筛查，属于由真实表列数据绘制的指标图，并非优化结构或反应路径图。',
        '新接触与原有键的同步响应将在第5节结合电子结构进一步讨论；静态几何只能用于筛选重排候选，不能给出转移路径或势垒。',
        '避免图4在图2、图3之前首次引用，保留静态证据的适用范围。')
replace(f, '图3-5并列展示两端Eb及两种差量。',
        '图3-5并列展示两端Eb及两种差量，全部配对数值见表1。',
        '补齐能量结果表的正文引用。')
replace(f, '两种指标对同一配对矩阵给出了不同的总体排序，说明“相互作用较强”与“净结合数值较低”不能在文字中混用。',
        '同一组两端构型在两种能量指标下呈现不同排序，表明Eint的数值优势不足以独立判断Eb所表征的端间差异。',
        '将编辑要求改写为数据直接支持的发现。')
replace(f, '图中没有为这些点添加未经计算的误差棒。',
        '这些点尚缺少相应的方法与环境敏感性评估。',
        '直接陈述小能差的证据缺口。')
replace(f, '图3-4与图5-1分端作图，并在本文中保留候选类别，而不使用全样本单一直线支持统一成键模型。',
        '图3-4分端比较内部键响应，强重排候选另见第5节；各类原子接触及候选类型需分别解释，现有数据不足以支持全样本统一成键关系。',
        '消除图4的提前引用，并说明分组的科学用途。')
replace(f, '结合图3-5和结构响应，下一步机制分析应集中于两个问题：一是为何部分构型具有更负Eint却没有更低Eb；二是为何部分H端终态表现出明显O—H伸长。前者需要EDA与能量参考态相结合，后者需要几何和电子结构的对应证据。二者可能有关，但目前不能把“更大形变”“更强极化”和“已经发生转移”写成同义结论。',
        '两端能量比较与几何响应提出了两个需要电子结构证据进一步解释的问题：部分构型为何具有更负Eint而没有更低Eb，以及三个H端候选为何出现显著O—H伸长。以下结合NBO、局部拓扑指标与完整EDA分项，分别考察供受体作用和分项抵消。相关讨论仍受能量参考态及分析条件可比性的限制；形变、极化与转移分别属于不同层次的判断。',
        '增强第3节到第4节的论证衔接。')
replace(f, '因而正文采用“占据供体轨道向相应反键轨道的作用”，保留实际LP或BD归属，不将局域化得到的成键轨道改写为不存在的LP(C)。',
        '因此，以下按原归属分别讨论LP或BD供体与相应反键轨道的作用，而不预设所有通道均由中心碳孤对电子主导。',
        '保留实际轨道归属，减少面向写作行为的说明。')
replace(f, '因此，本文不绘制全体系WBI趋势图，也不把缺失的键级证据写成已完成验证。',
        '现有WBI仅能描述H-CO的局部键级，尚不足以检验全系列趋势或完成三个H端候选及Cl-NHCme的新旧键对照。',
        '将制图行为说明改为键级证据的覆盖范围。')
replace(f, '图4-8选择CO、N2CAACme、PPh3、NHCme和CAACmeSPh2各两端，保留全部五项并独立标出总量。',
        '图4-8和表2比较CO、N2CAACme、PPh3、NHCme和CAACmeSPh2各两端，保留全部五项并独立标出总量。',
        '补齐代表构型EDA表的正文引用。')
replace(f, '目的是比较吸引与排斥抵消，而非以最大负项给作用“定性”。',
        '用于比较吸引与排斥的抵消；整体作用性质仍需结合各分项和总量判断。',
        '改为正式学术表述。')
replace(f, '因此，本文不绘制推测性的NOCV等值面，也不凭NBO通道标签反向生成NOCV轨道图。',
        '缺少轨道对编号、分通道能与形变密度，使现有NOCV字段尚不能用于空间供受体机制分析。',
        '明确缺失数据影响的科学问题。')
replace(f, '电子耗尽/积累方向是否与NBO识别的O—H或O—Cl反键给予一致。',
        '电子耗尽与积累方向是否与NBO识别的向O—H或O—Cl反键轨道供电子的方向一致。',
        '补齐供电子表述中的语法和轨道对象。')
replace(f, '由于缺少原始BCP身份，本文保留两值，将其列作核查点，不以猜测数字修正，也不选择性忽略它来宣称证据完全一致。',
        '该差异在BCP身份、导出过程及原始数值复核前尚无确定解释，因而两体系的拓扑证据不能视为完全一致。',
        '保留异常与解释边界，去除重复的核查操作口吻。')
replace(f, '## 5 强相互作用候选中的质子重新定位与C—Cl成键证据',
        '## 5 强相互作用候选的结构重排与电子证据',
        '标题与内文候选判断保持同等主张强度。')
replace(f, '本文不根据端点虚构势垒或速率。',
        '静态端点尚不提供势垒或速率信息。',
        '以证据限制替代写作行为声明。')
replace(f, '不能仅由外部接触数据量化新旧键强弱的转移。',
        '仅有外部接触数据，尚不能量化新接触增强与原有O—Cl键削弱的程度。',
        '避免将未确认的新接触直接表述为已成键。')
replace(f, 'C(NHCMe)2与ClOH', 'C(NHCMe)₂与ClOH', '统一文献模型的下标；不改原始体系标签大小写。')
replace(f, '以C(NHCMe)2为例', '以C(NHCMe)₂为例', '统一文献模型的下标。')

f = 'components/06_conclusions.md'
replace(f, '这样能够直接回答排序反转与成键分类两个关键问题，比增加大量缺乏明确用途的计算更有效。',
        '该补充方案分别针对排序反转与成键分类，能够以有限的补充资料和计算检验当前解释。',
        '直接说明最小补充的用途。')

# Number by the actual order of first reference and display, independent of asset IDs.
number_map = {'图3-4':'图1', '图3-5':'图2', '图4-8':'图3', '图5-1':'图4', '表5-1':'表3'}
path = ROOT/'components/03_05_results.md'
text = path.read_text()
for old, new in number_map.items(): text = text.replace(old, new)
path.write_text(text)
changes.append(dict(file=str(path.relative_to(ROOT)),before=number_map,after='图1—4、表1—3连续编号',reason='按实际首引和插入顺序修正跳号；内部F1/F2资产名称保留。'))
captions = json.loads((ROOT/'data/figure_captions.json').read_text())
for stem, (title, caption) in captions.items():
    for old, new in number_map.items(): title = title.replace(old, new)
    for code in ['F1','F2','F3','F4']: title = title.replace('（'+code+'）','')
    caption = caption.replace('单位限制同F3。','单位限制同图3。')
    captions[stem] = [title,caption]
(ROOT/'data/figure_captions.json').write_text(json.dumps(captions,ensure_ascii=False,indent=2))

f = 'scripts/assemble_final.py'
replace(f, "def mdtable(name):\n rows=tables[name]", "table_titles={'表3-1':'表1 两端能量及配对差量','表4-3':'表2 代表构型的EDA五分项与总量','表5-1':'表3 强相互作用候选与参照构型的联合证据'}\ndef mdtable(name):\n rows=tables[name]", '保留历史缓存键，增加完整连续表题。')
replace(f, "return '\\n\\n'+name+'\\n\\n| '", "return '\\n\\n'+table_titles[name]+'\\n\\n| '", 'Word、PDF与Markdown统一使用完整表题。')
replace(f, "limits=(R/'data/requirements_source.md').read_text()", "limits=(R/'data/requirements_source.md').read_text().replace('# 第二阶段待核实与最小补充清单','# 全稿待核实与最小补充清单')", '重建时保留全稿待核实清单标题。')
replace(f, '因为没有路径及充分新旧键证据。', '并使用“强相互作用候选的结构重排与电子证据”，因为缺少路径和充分的新旧键证据。', '保留原大纲与本轮第5节标题的对应关系。')

f = 'scripts/plot_figures.py'
for old,new in [('F1  H-end / Cl-end energy comparison','Fig. 2  H-end / Cl-end energy comparison'),('F2  Internal-bond response to complex formation','Fig. 1  Internal-bond response to complex formation'),('F3  Five-component EDA: stabilization and cancellation','Fig. 3  Five-component EDA: stabilization and cancellation'),('F4  Geometry screening of strongly reorganized candidates','Fig. 4  Geometry screening of strongly reorganized candidates')]:
    replace(f,old,new,'同步成图标题与正文编号，绘图值、分组和坐标保持不变。')
replace(f, 'python /workspace/zxj/report2/scripts/plot_figures.py', 'python stage6_revision/scripts/plot_figures.py', '更正本轮复现命令。')

(ROOT/'data/revision_changes.json').write_text(json.dumps(changes,ensure_ascii=False,indent=2))
print(f'Applied/documented {len(changes)} editorial revisions; source numeric data retained.')
