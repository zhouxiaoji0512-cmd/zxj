from pathlib import Path
import json,datetime,hashlib
p=Path('/tmp/stage6_bib')
refs=json.loads(Path('/workspace/zxj/final_paper/audit/references.json').read_text())['references']
results=json.loads((p/'crossref_results.json').read_text())
all_attempts=[]
for f in sorted(p.glob('*_retrieval.json')):
 d=json.loads(f.read_text());d['retrieval_record_file']=str(f);all_attempts.append(d)
entries=[]
for r in refs:
 entry={'id':r['id'],'doi':r['doi'],'online_verified':False,'online_verification_status':'blocked_at_proxy_no_metadata_received','verified_metadata_additions':{},'local_uploaded_source_baseline':{k:r.get(k) for k in ['source_file','authors','title','year','journal','volume','pages','article_number','bibliographic_status']},'attempts':[a for a in all_attempts if a.get('id')==r['id'] or a.get('label','').startswith(r['id']+'_')]}
 entries.append(entry)
out={'schema_version':1,'retrieval_date_client_Asia_Shanghai':'2026-10-19','scope':'DOI/出版社/Crossref官方书目元数据在线补核；并未在线阅读全文。','overall_result':'blocked','source_baseline_file':'/workspace/zxj/final_paper/audit/references.json','source_baseline_sha256':hashlib.sha256(Path('/workspace/zxj/final_paper/audit/references.json').read_bytes()).hexdigest(),'newly_verified_count':0,'references':entries,'network_note':'所有HTTPS请求在代理CONNECT阶段403，未收到Crossref/DOI出版社远端元数据响应。HTTP接口请求返回403；保存错误响应本体。此处HTTP403不是出版社/论文不存在的证据。','attempt_count':len(all_attempts)}
(p/'verified.json').write_text(json.dumps(out,ensure_ascii=False,indent=2))
lines=['# 第六阶段书目在线补核记录','','检索日期：2026年10月19日（Asia/Shanghai）。','','## 结论','','未取得任何新的官方书目元数据。11条Crossref官方API请求以及针对R04、R11的DOI和出版社请求均受网络代理限制。HTTPS在CONNECT阶段返回403；HTTP接口请求亦返回403。因此，R04最终卷页、R11最终页码仍为【待核实】，不得补填，也不得把此次检索写成已核实出版社信息。','','R04、R11的作者、题名、年份等原有字段仅沿用已上传稿及既有核查清单；本轮没有在线独立确认。这些值与新确认数据分开保存于 `verified.json` 的 `local_uploaded_source_baseline`，`verified_metadata_additions` 保持空对象。','','## 重点条目','','|标识|已上传来源的题名|DOI|需补核字段|本轮结果|','|---|---|---|---|---|']
for r in refs:
 if r['id'] in ('R04','R11'):
  missing='正式卷、期、页码或文章号' if r['id']=='R04' else '正式期、页码或文章号'
  lines.append(f"|{r['id']}|{r['title']}|{r['doi']}|{missing}|代理限制，未取得元数据|")
lines+=['','## 其余9篇与请求记录','','对其余9篇各请求一次Crossref官方works接口，仅作书目元数据核对尝试；未收到元数据，因此不能报告作者、卷页等字段在线核对成功。原有基于上传PDF的核查结论不因网络失败而改变。','','|请求记录|来源URL|结果|','|---|---|---|']
for a in all_attempts:
 label=a.get('id',a.get('label'))
 lines.append(f"|{label}|{a['source_url']}|{a.get('error','HTTP '+str(a.get('status_code')))}|")
lines+=['','## 证据文件与边界','','- `/tmp/stage6_bib/verified.json`：机器可读结果，新增核实项为0；保留已有来源字段并明确其来源边界。','- `/tmp/stage6_bib/*_retrieval.json`：每次请求的URL、检索UTC时刻与错误。','- `/tmp/stage6_bib/R04_crossref_http_response.txt`：HTTP接口错误响应本体；HTTPS代理拒绝时没有远端响应本体，未伪造或补造。','- `/tmp/stage6_bib/check.py`、`secondary.py`、`finalize.py`：复现脚本；仅依赖Python标准库。','','需要具备可访问Crossref/doi.org/出版社的网络，或提供R04、R11最终出版PDF/官方书目导出，才能解决所缺卷页。本轮未修改原稿、参考文献正文或任何仓库数据。']
Path('/tmp/stage6_bib_review.md').write_text('\n'.join(lines)+'\n')
print(json.dumps({'attempt_count':len(all_attempts),'verified_count':0,'report':'/tmp/stage6_bib_review.md','machine_readable':'/tmp/stage6_bib/verified.json'},ensure_ascii=False))
