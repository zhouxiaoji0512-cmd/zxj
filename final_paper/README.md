# 最终交付：HOCl与碳(0)化合物间氢键和卤键竞争

本目录完成第三阶段全文整合、第四阶段数值与引文审校、第五阶段排版和交付核验。文件属于完整论文初稿；原始作业设置、若干单位及候选成键性质仍有【待核实】项目，不能因排版完成而视为已核实的投稿定稿。

## 优先阅读

- 完整论文初稿.docx：可编辑全文，沿原大纲六章，含中文摘要、关键词、4张正文图、3张结果表及顺序编码参考文献。
- 完整论文初稿.pdf：相同内容的阅读版。
- 补充材料.docx / 补充材料.pdf：逐值来源说明、2张补充图、统计口径、最小补充清单及书目缺口。
- 数据总表.xlsx：17张工作表，保留全部原值，含56条构型、28对能量及2733条正文来源索引。
- 图注.md、参考文献.docx/CSV/Markdown、待核实事项.md、原始资料清单.csv、大纲对应关系.md。
- 审校与交付说明.md：第三至五阶段成果、字数口径和验证范围。
- 论文最终交付包.zip：上述全部成果、源文件和脚本的完整归档；文件清单.json记录逐文件SHA-256。

正文汉字与含图表说明汉字分别统计于data/manuscript_counts.json，英文、数字另计；未以参考文献英文篇幅冒充约1.5万字中文正文。文献按GB/T7714—2015顺序编码，用上角标，原R01—R11与最终编号的对应见data/citation_map.json。

## 图与数据

figures/包含6图各自的300dpi PNG、保留文字的SVG及单页PDF。复杂图可使用原尺寸矢量版本查看或重新排版。所有图为实表数值的审阅图；未伪造优化结构、轨道或NOCV等值面。未知单位保留原字段说明，不自行补Å、a.u.或e。

data/保留冻结JSON/CSV、逐图输入和逐值来源。母体完整组成、能量参考及异常项详见待核实事项；bess原值未改。R12编辑占位稿及两份只有SI的记录没有冒充已核定正文文献。当前书目核实以上传PDF为准。

## 复现

Python依赖版本见scripts/requirements.txt。全文PDF另需Pandoc、XeLaTeX、Noto Serif/Sans CJK SC字体；Word使用统一A4学术排版，没有声称符合特定学校或期刊模板。

```bash
python final_paper/scripts/assemble_final.py
python final_paper/scripts/render_final.py
python final_paper/scripts/plot_figures.py
python final_paper/scripts/validate_final.py
```

重绘后若需更新嵌图，再执行render_final.py。本目录带有文稿组件与缓存图注/表格，因此绘图和文稿导出可直接使用交付包；对照原始工作簿及哈希的严格校验需要仓库中的原件。enrich_data.py用于在原仓库中更新数据总表的全稿引文和说明，不新增量化计算。

components/为可编辑章节源文件；audit/保留独立数值和文献审校、排版日志及页面预览。审校通过仅表示陈述与已有资料对应、算术和文件通过检查，不表示未提供的计算已补做。
