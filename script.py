## remember env\Scripts\activate.bat before starting

import requests
from urllib.parse import quote

# for later
base = 'https://api.plazi.org/v1'
format = '&format=json'

#see also the SANBI taxonomy API at https://taxonomy.sanbi.org.za/


article_doi = '10.1600/036364422X16674053033831'
article_endpoint = 'http://tb.plazi.org/GgServer/dioStats/stats?outputFields=doc.articleUuid+doc.doi+bib.author+bib.title+bib.year+bib.source+bib.volume+bib.issue+bib.numero+bib.firstPage+bib.lastPage+cont.treatCount+cont.matCitCount&groupingFields=doc.articleUuid+doc.doi+bib.author+bib.title+bib.year+bib.source+bib.volume+bib.issue+bib.numero+bib.firstPage+bib.lastPage+cont.treatCount+cont.matCitCount&FP-doc.doi={}&format=JSON'.format(quote(article_doi, safe=''))

# uncertain what the correct parameter name is here for the article UUID, this isn't working 
treatments_endpoint = 'http://api.plazi.org/v1/treatments/search?article-uuid={}&format=JSON'

### SCRIPT ###

# print('Fetching article record at the URL below:')
# print()
# print(article_endpoint)
# print()

#get the article uuid
# article_response = requests.get(article_endpoint)
# if article_response.ok:
#   results = article_response.json()
#   articles = results['data']
#   if articles:
#     article_uuid = articles[0]['DocArticleUuid'] # there should only be one...
#   else:
#     print('article not found...')
# else:
#   print('Oops! Something went wrong getting the article...')
#   print(article_response.content.decode('utf-8'))

# use uuid here

print("fetching treatments")
# we can't get a uuid using the above as yet so let's set it manually here for now...
article_uuid = 'FFA0FFFBF17DA82EFFA4FF9BFF8EFFA8' #still the Chamaecrista article

treatments_response = requests.get(treatments_endpoint.format(article_uuid))
if treatments_response.ok:
  results = treatments_response.json()
  treatments = results['data']
  if treatments:
    treatment_uuid = treatments[0]['TreatmentUuid'] # there should only be one...
  else:
    print('treatments not found...')
else:
  print('Oops! Something went wrong getting treatments...')
  print(treatments_response.content.decode('utf-8'))



