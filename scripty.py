## remember env\Scripts\activate.bat before starting

import requests

base = 'https://api.plazi.org/v1'
format = '&format=json'

# just for testing out requests, will remove shortly
PIXABAY_API_KEY = "11111111-7777777777777777777777777"
base_url = "https://pixabay.com/api/"
base_params = {
    "key": PIXABAY_API_KEY,
    "q": "fruit",
    "image_type": "photo",
    "category": "food",
    "safesearch": "true"
}

response = requests.get(base_url, params=base_params)
if response.ok:
  results = response.json()
  i = 1
else:
  print('Oops!', response.content.decode('utf-8'))
