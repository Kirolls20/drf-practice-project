import requests

endpoint = 'http://localhost:8000/api/'

response = requests.post(endpoint,params={'ab':12},json={'title':'hello Server!','price':'11'})
print(response.json())
print(response.status_code)

