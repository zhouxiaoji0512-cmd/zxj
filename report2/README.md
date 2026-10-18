# 第二阶段交付：关键图表与结果讨论

本目录基于report1资料和原始工作簿，完成原大纲第3—5章的结果与讨论限定初稿。数据均按作者已确认的独立计算来源记录，bess原值全部保留。本稿仍为审阅版，尚未整合为完整约1.5万字论文。

主要文件：

- 结果与讨论_第二阶段.docx：可编辑Word，含4张正文图、2张补图、3张结果表和来源索引概要。
- 结果与讨论_第二阶段.md：正文源稿；结果与讨论_含图表.md含完整图表和文献。
- 统一数据总表_第二阶段.xlsx：保留第一阶段10张表，增加逐值来源、结果表及图注。
- 图注_第二阶段.md、参考文献_第二阶段.md、待核实与最小补充清单.md。
- figures/：6图各含PNG(300dpi)、SVG(保留文字)和单页PDF。
- data/figure_*.csv：每图输入及来源，complexes/pairs/provenance等JSON/CSV为冻结数据。
- data/数据来源索引.csv：正文D01—D17逐值对应文件、工作表和单元格。
- notes/：资料读取、独立分析、文献页表证据及恢复记录。

图号映射：F1→图3-5（合并原3-6），F2→图3-4，F3→图4-8，F4→图5-1。F4为真实几何数据的筛查图，不能当优化结构图或密度图。

## 复现

当前环境已具备依赖，版本见scripts/requirements.txt。仅重绘可使用本目录的冻结JSON；完整重建需在包含report1和原始资料的仓库中运行：

```bash
python report2/scripts/prepare_data.py
python report2/scripts/plot_figures.py
python report2/scripts/build_manuscript.py
python report2/scripts/validate_deliverables.py
```

图中使用英文标签，附中文图注；Word为统一A4排版，未声称符合学校或期刊特定模板。图表没有补造误差棒、缺失NOCV密度或优化坐标。Eb−Eint仅称表列差量；ECORR不改称纯色散；未核实单位不默认加Å、a.u.或e。

本目录在2026-10-18按对话保留正文及历史绘图脚本恢复，见notes/恢复记录.md；重新检查了原表数值、图像和文件完整性，不声称与丢失二进制文件逐字节相同。
