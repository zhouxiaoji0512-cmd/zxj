from pathlib import Path
import json,urllib.request,urllib.error,datetime,concurrent.futures,time,hashlib
out=Path('/tmp/stage6_bib')
refs=json.loads(Path('/workspace/zxj/final_paper/audit/references.json').read_text())['references']
def fetch(r):
 url='https://api.crossref.org/works/'+r['doi']
 t=datetime.datetime.now(datetime.timezone.utc).isoformat()
 try:
  res=urllib.request.urlopen(urllib.request.Request(url,headers={'User-Agent':'ScholarlyBibliographyAudit/1.0','Accept':'application/json'}),timeout=55)
  content=res.read()
  status=res.status
  (out/(r['id']+'_crossref_response.json')).write_bytes(content)
  meta={'id':r['id'],'doi':r['doi'],'source_url':url,'retrieved_at_utc':t,'status_code':status,'response_sha256':hashlib.sha256(content).hexdigest()}
  if status==200:
   msg=json.loads(content)['message']
   meta['crossref_metadata']={k:msg.get(k) for k in ['DOI','title','author','container-title','short-container-title','publisher','volume','issue','page','article-number','published','published-online','published-print','issued','link','resource','URL','type','created','deposited']}
  else:meta['error']=content.decode('utf-8',errors='replace')[:250]
 except Exception as e:meta={'id':r['id'],'doi':r['doi'],'source_url':url,'retrieved_at_utc':t,'error':str(e)}
 (out/(r['id']+'_retrieval.json')).write_text(json.dumps(meta,ensure_ascii=False,indent=2))
 return meta
with concurrent.futures.ThreadPoolExecutor(max_workers=6) as ex:
 results=list(ex.map(fetch,refs))
(out/'crossref_results.json').write_text(json.dumps(results,ensure_ascii=False,indent=2))
for r in results:
 print(r['id'],r.get('status_code'),json.dumps(r.get('crossref_metadata',r.get('error')),ensure_ascii=False))
