## 附录A 定量陈述来源表

[Dxx]指向data/数据来源索引.csv；每条包含体系、指标、原值、原表单元格。下面给出用途和核心来源范围，逐值表为机器可复核版本。

|索引|对应内容|原始来源|
|---|---|---|
|D01|体系命名、覆盖与频率汇总|HOClxlsx.xlsx：NBO主表、编号对照；逐值单元格见CSV|
|D02|MEP原字段及反例|HOClxlsx.xlsx：MEP；逐值单元格见CSV|
|D03|全部几何、基准与距离差|HOClxlsx.xlsx：结构数据；逐值单元格见CSV|
|D04|全28对能量排序及范围|HOClxlsx.xlsx：bess；逐值单元格见CSV|
|D05|九对反转与Eb-Eint表列差量|HOClxlsx.xlsx：bess；逐值单元格见CSV|
|D06|正或近零结合量|HOClxlsx.xlsx：bess；逐值单元格见CSV|
|D07|NBO通道身份、计数和E2|HOClxlsx.xlsx：NBO主表；逐值单元格见CSV|
|D08|CT端比较及与Eb反例|HOClxlsx.xlsx：NBO、bess；逐值单元格见CSV|
|D09|局部拓扑符号与rho可疑差异|HOClxlsx.xlsx：AIM、结构数据；逐值单元格见CSV|
|D10|WBI可用与缺失|HOClxlsx.xlsx：结构数据；逐值单元格见CSV|
|D11|EDA完整求和与跨表差|HOClxlsx.xlsx：EDA、bess；逐值单元格见CSV|
|D12|代表体系EDA及配对抵消|HOClxlsx.xlsx：EDA、bess；逐值单元格见CSV|
|D13|NOCV Energy字段，含义未知|HOClxlsx.xlsx：NOCV；逐值单元格见CSV|
|D14|三个H端优先强重排候选|HOClxlsx.xlsx：AIM、NBO、NBO主表、bess、结构数据；逐值单元格见CSV|
|D15|Cl-NHCme重点个案|HOClxlsx.xlsx：AIM、NBO、NBO主表、bess、结构数据；逐值单元格见CSV|
|D16|按名称对应系列及混配比较|HOClxlsx.xlsx：NBO、bess、结构数据；逐值单元格见CSV|
|D17|近零端间差|HOClxlsx.xlsx：bess；逐值单元格见CSV|

衍生量统一为δb=Eb(H)−Eb(Cl)、δint=Eint(H)−Eint(Cl)、g=Eb−Eint、R=EDA_E−Σ5。D05表列差量未自动命名形变能；D11/S1的舍入界限仅用于算术审计。任何BCP、CT或NOCV字段身份未核实处均不得据文献反填。
