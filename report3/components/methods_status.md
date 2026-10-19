# 方法章节核查状态

产物：`components/02_methods.md`。保留原大纲2.1—2.8，正文约1,941个汉字（不含拉丁字符的统计），全文约2,924个字符。采用{{R01}}、{{R02}}、{{R06}}文献占位及[Dxx]来源组，不预先重排参考文献号。

## 本轮实际读取

- `论文大纲.docx`全文、原第2章方法表以及大纲与参考文献设置的归属提示。
- `report1/第一阶段核查报告.docx`正文及表格；另读其保存在`report2/notes/report1_audit.txt`的文本用于精确定位。
- `report1/统一数据总表_第一阶段.xlsx`及`report2/统一数据总表_第二阶段.xlsx`的表结构；读取原始`HOClxlsx.xlsx`的NBO主表、bess、EDA、结构数据、NOCV表头及代表行，确认NBO受体为BD*而非BD。
- `report2/data/metric_dictionary.csv`全表、`report2/待核实与最小补充清单.md`、`report2/数据来源说明.md`。
- `report2/scripts/prepare_data.py`、`plot_figures.py`、`validate_deliverables.py`及既有`validation_report.json`。绘图脚本实际从冻结JSON读取并输出逐图CSV，方法稿未误写成仅从CSV读取。
- `report2/data/references.csv`的R01、R02、R06用途和边界；本轮未额外声称重新通读对应PDF。

## 写法约束及处理

|问题|本稿处理|
|---|---|
|实际运行参数不可核实|大纲声明与已验证方法严格分开；集中保留【待核实—运行条件】，不默认补足软件版本、泛函、基组、色散、溶剂或收敛值。|
|Eint/Eb公式未明确|仅列待确认统一方案；当前实际定义为δb、δint及g的算术差，不称g为形变能。|
|频率汇总|仅写56条汇总虚频为零、最低频率为正，不称已逐作业复验。|
|单位缺失|距离/角度不擅写Å或度；AIM、CT、NOCV定义与单位保留缺口；EDA只ES明示单位。|
|能量分解|完整ES、EX、REP、POL、ECORR及闭合残差；不省EX，不叫ECORR纯色散，不将POL等同ETS轨道能。|
|NBO/WBI|E(2)不叫结合能；LP与BD供体均保留，受体为相应BD*；WBI缺失不填零。|
|强候选|几何筛选不等于转移归属；未标记点也不自动称弱作用。|
|复现边界|说明JSON/CSV、Matplotlib与SHA-256的实际链路；源数据/图表检查不等于原始量化作业验证。|

本轮未重算量子化学作业、未改动原数据或report1/report2文件、未执行Git提交。方法参数与原子对应仍应通过原始日志/坐标补齐；现有缺口不阻止其余有证据内容整合。
