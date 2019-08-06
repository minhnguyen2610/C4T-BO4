import json
import requests
r = requests.get('https://jsonplaceholder.typicode.com/users')
#request getting info from a website
print(r.json)


