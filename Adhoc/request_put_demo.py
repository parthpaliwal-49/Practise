import requests
import json
BASE_URL = 'https://jsonplaceholder.typicode.com/'
url_post = BASE_URL + 'posts/2'
# response = requests.post(url_post)

put_post = {
    'userId' : 1,
    'title': 'demo title',
    'body': 'demo body - updated'
}

response = requests.put(url_post, data=put_post)
print(response.status_code)
print(response.text)



