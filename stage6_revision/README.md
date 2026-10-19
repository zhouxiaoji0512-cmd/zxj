# 第六阶段：通用修订及期刊适配准备

基线为main提交020f74d中的final_paper；上一版完整保留。本目录完成通用语言、论证衔接、图表连续编号、结果表引用和数据字典说明修订。用户已选择按指定期刊修订，尚未提供期刊名称；本轮不声称符合任何具体期刊指南，也未提交稿件。

- 完整论文修订稿.docx / .pdf：本轮全文，沿原六章大纲，保留所有影响判断的待核实事项。
- 本轮修订说明.docx / .md：实际修改及尚未完成的期刊适配范围。
- 数据总表.xlsx：19张工作表，保留原始数值与历史计划；新增本轮图表索引和修订说明。
- 作者确认表.docx / .md：待填期刊和最小必要资料，已确认的信息不再重复询问。
- 补充材料、参考文献、图注、待核实事项及原始资料清单：科学证据与来源记录。
- figures/：4张正文图、2张补充图的PNG/SVG/PDF；本轮仅同步标题编号，不改绘图数值或分组。
- data/：冻结数据、逐值来源、修改清单及实际成图索引；figure_plan.*为历史方案。
- audit/：baseline_*是上一版审校，不能误读为本轮审校；本轮结果另记。

图1对应内部F2，图2对应F1，图3对应F3，图4对应F4；历史表3-1/4-3/5-1依次为本轮表1/2/3。D01—D17仍是内部数据来源编码，文献上角标采用独立顺序编码，二者不混编。待期刊明确后再决定正文和补充材料中的来源标记呈现方式。

## 复现

依赖见scripts/requirements.txt，PDF另需Pandoc、XeLaTeX及Noto CJK字体。编辑后的章节组件和图注缓存已随本目录保存，通常运行：

```bash
python stage6_revision/scripts/assemble_final.py
python stage6_revision/scripts/enrich_data.py
python stage6_revision/scripts/update_revision_index.py
python stage6_revision/scripts/plot_figures.py
python stage6_revision/scripts/render_final.py
python stage6_revision/scripts/validate_final.py
```

enrich_data.py及原件逐值比对需仓库中的源文件。apply_stage6_revision.py记录从旧版到本轮的精确替换，不作为重建已修订组件的必要步骤。数值原值未改；实际量子化学作业未补做；缺失的定义和成键证据不会因语言、版式修订而自动核实。
