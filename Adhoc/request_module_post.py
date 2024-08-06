import requests
import json
BASE_URL = 'https://jsonplaceholder.typicode.com/'
url_post = BASE_URL + 'posts'
url_comments = BASE_URL + 'comments'
new_post = {
    'userId' : 1,
    'title': 'demo title',
    'body': 'demo body'
}

response = requests.post(url_post, data=new_post)
print(response.status_code)
print(response.text)



