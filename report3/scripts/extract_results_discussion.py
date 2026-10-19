#!/usr/bin/env python3
"""Extract the stage 3–5 discussion without changing its text or numbering."""
from pathlib import Path
import re

R=Path(__file__).resolve().parents[1]
text=(R/'论文_图文整合.md').read_text()
start=re.search(r'^## 3 ',text,re.M)
end=re.search(r'^## 6 ',text,re.M)
assert start and end and start.start()<end.start()
discussion=text[start.start():end.start()].strip()
preface=('# 结果与讨论（第三至第五阶段归档版）\n\n'
         '本文件从完整论文初稿第3—5章逐字提取，保留原图表、内部数据来源编码及全稿参考文献编号。'
         '文末附全稿参考文献清单以便与完整初稿对应；完整方法与其余章节见《完整论文初稿》。'
         '计算方法、能量参考、部分单位及强重排候选性质的待核实限定继续有效。\n\n')
(R/'结果与讨论_第三至五阶段.md').write_text(preface+discussion+'\n\n'+(R/'参考文献.md').read_text())
print('Extracted unchanged chapters 3–5 with 4 figures, 3 tables and original citation numbering.')
