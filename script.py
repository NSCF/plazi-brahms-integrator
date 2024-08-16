## remember env\Scripts\activate.bat before starting

import requests
from urllib.parse import quote


article_doi = '10.1600/036364422X16674053033831'



article_endpoint = 'http://tb.plazi.org/GgServer/dioStats/stats?outputFields=doc.articleUuid+doc.doi+bib.author+bib.title+bib.year+bib.source+bib.volume+bib.issue+bib.numero+bib.firstPage+bib.lastPage+cont.treatCount+cont.matCitCount&groupingFields=doc.articleUuid+doc.doi+bib.author+bib.title+bib.year+bib.source+bib.volume+bib.issue+bib.numero+bib.firstPage+bib.lastPage+cont.treatCount+cont.matCitCount&FP-doc.doi={}&format=JSON'.format(quote(article_doi, safe=''))

# for later
base = 'https://api.plazi.org/v1'
format = '&format=json'

### SCRIPT ###
print('Fetching article record at the URL below:')
print()
print(article_endpoint)
print()

#get the article uuid
article_response = requests.get(article_endpoint)
if article_response.ok:
  results = article_response.json()
  articles = results['data']
  if articles:
    article_uuid = articles[0]['DocArticleUuid'] # there should only be one...
  else:
    print('article not found...')
else:
  print('Oops! Something went wrong...')
  print(article_response.content.decode('utf-8'))

# use uuid here
