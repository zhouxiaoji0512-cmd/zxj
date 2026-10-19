# 第六阶段书目在线补核记录

检索日期：2026年10月19日（Asia/Shanghai）。

## 结论

未取得任何新的官方书目元数据。11条Crossref官方API请求以及针对R04、R11的DOI和出版社请求均受网络代理限制。HTTPS在CONNECT阶段返回403；HTTP接口请求亦返回403。因此，R04最终卷页、R11最终页码仍为【待核实】，不得补填，也不得把此次检索写成已核实出版社信息。

R04、R11的作者、题名、年份等原有字段仅沿用已上传稿及既有核查清单；本轮没有在线独立确认。这些值与新确认数据分开保存于 `verified.json` 的 `local_uploaded_source_baseline`，`verified_metadata_additions` 保持空对象。

## 重点条目

|标识|已上传来源的题名|DOI|需补核字段|本轮结果|
|---|---|---|---|---|
|R04|Complexes between hypohalous acids and phosphine derivatives. Pnicogen bond versus halogen bond versus hydrogen bond|10.1016/j.saa.2014.05.001|正式卷、期、页码或文章号|代理限制，未取得元数据|
|R11|Establishing Halogen-Bond Preferences in Molecules with Multiple Acceptor Sites|10.1002/cplu.202100102|正式期、页码或文章号|代理限制，未取得元数据|

## 其余9篇与请求记录

对其余9篇各请求一次Crossref官方works接口，仅作书目元数据核对尝试；未收到元数据，因此不能报告作者、卷页等字段在线核对成功。原有基于上传PDF的核查结论不因网络失败而改变。

|请求记录|来源URL|结果|
|---|---|---|
|R01|https://api.crossref.org/works/10.1039/d6sc02210c|<urlopen error Tunnel connection failed: 403 Forbidden>|
|R02|https://api.crossref.org/works/10.1021/jp806101t|<urlopen error Tunnel connection failed: 403 Forbidden>|
|R03|https://api.crossref.org/works/10.1007/s00894-013-1969-7|<urlopen error Tunnel connection failed: 403 Forbidden>|
|R04_crossref_http|http://api.crossref.org/works/10.1016/j.saa.2014.05.001|HTTP Error 403: Forbidden|
|R04_doi|https://doi.org/10.1016/j.saa.2014.05.001|<urlopen error Tunnel connection failed: 403 Forbidden>|
|R04_elsevier|https://linkinghub.elsevier.com/retrieve/doi/10.1016/j.saa.2014.05.001|<urlopen error Tunnel connection failed: 403 Forbidden>|
|R04|https://api.crossref.org/works/10.1016/j.saa.2014.05.001|<urlopen error Tunnel connection failed: 403 Forbidden>|
|R05|https://api.crossref.org/works/10.1039/d4cp03894k|<urlopen error Tunnel connection failed: 403 Forbidden>|
|R06|https://api.crossref.org/works/10.1002/asia.202301106|<urlopen error Tunnel connection failed: 403 Forbidden>|
|R07|https://api.crossref.org/works/10.1021/jacs.3c11449|<urlopen error Tunnel connection failed: 403 Forbidden>|
|R08|https://api.crossref.org/works/10.3390/molecules26071885|<urlopen error Tunnel connection failed: 403 Forbidden>|
|R09|https://api.crossref.org/works/10.1039/c6ce02089e|<urlopen error Tunnel connection failed: 403 Forbidden>|
|R10|https://api.crossref.org/works/10.1021/cg500094b|<urlopen error Tunnel connection failed: 403 Forbidden>|
|R11_crossref_doi|https://doi.org/10.1002/cplu.202100102|<urlopen error Tunnel connection failed: 403 Forbidden>|
|R11_doi|https://doi.org/10.1002/cplu.202100102|<urlopen error Tunnel connection failed: 403 Forbidden>|
|R11|https://api.crossref.org/works/10.1002/cplu.202100102|<urlopen error Tunnel connection failed: 403 Forbidden>|
|R11_wiley|https://chemistry-europe.onlinelibrary.wiley.com/doi/10.1002/cplu.202100102|<urlopen error Tunnel connection failed: 403 Forbidden>|

## 证据文件与边界

- `/tmp/stage6_bib/verified.json`：机器可读结果，新增核实项为0；保留已有来源字段并明确其来源边界。
- `/tmp/stage6_bib/*_retrieval.json`：每次请求的URL、检索UTC时刻与错误。
- `/tmp/stage6_bib/R04_crossref_http_response.txt`：HTTP接口错误响应本体；HTTPS代理拒绝时没有远端响应本体，未伪造或补造。
- `/tmp/stage6_bib/check.py`、`secondary.py`、`finalize.py`：复现脚本；仅依赖Python标准库。

需要具备可访问Crossref/doi.org/出版社的网络，或提供R04、R11最终出版PDF/官方书目导出，才能解决所缺卷页。本轮未修改原稿、参考文献正文或任何仓库数据。
