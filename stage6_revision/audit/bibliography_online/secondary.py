from pathlib import Path
import urllib.request,urllib.error,json,datetime,concurrent.futures,hashlib
out=Path('/tmp/stage6_bib')
tasks=[('R04_doi','https://doi.org/10.1016/j.saa.2014.05.001','text/html'),('R11_doi','https://doi.org/10.1002/cplu.202100102','text/html'),('R04_elsevier','https://linkinghub.elsevier.com/retrieve/doi/10.1016/j.saa.2014.05.001','text/html'),('R11_wiley','https://chemistry-europe.onlinelibrary.wiley.com/doi/10.1002/cplu.202100102','text/html'),('R04_crossref_http','http://api.crossref.org/works/10.1016/j.saa.2014.05.001','application/json'),('R11_crossref_doi','https://doi.org/10.1002/cplu.202100102','application/vnd.citationstyles.csl+json')]
def fetch(task):
 label,url,accept=task
 m={'label':label,'source_url':url,'accept':accept,'retrieved_at_utc':datetime.datetime.now(datetime.timezone.utc).isoformat()}
 try:
  with urllib.request.urlopen(urllib.request.Request(url,headers={'User-Agent':'Mozilla/5.0','Accept':accept}),timeout=45) as r:
   content=r.read()
   m.update(status_code=r.status,final_url=r.url,content_type=r.headers.get('Content-Type'),sha256=hashlib.sha256(content).hexdigest())
   (out/(label+'_response.txt')).write_bytes(content)
 except urllib.error.HTTPError as e:
  m.update(status_code=e.code,error=str(e))
  content=e.read()
  (out/(label+'_response.txt')).write_bytes(content)
 except Exception as e:m['error']=str(e)
 (out/(label+'_retrieval.json')).write_text(json.dumps(m,ensure_ascii=False,indent=2))
 return m
with concurrent.futures.ThreadPoolExecutor(max_workers=6) as ex:
 results=list(ex.map(fetch,tasks))
print(json.dumps(results,ensure_ascii=False,indent=2))
