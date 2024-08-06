import requests
import json
BASE_URL = 'https://jsonplaceholder.typicode.com/'
url_post = BASE_URL + 'posts/2'
# response = requests.post(url_post)

response = requests.delete(url_post)
print(response.status_code)
print(response.text)



