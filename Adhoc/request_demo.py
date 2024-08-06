import requests
import json
BASE_URL = 'https://jsonplaceholder.typicode.com/'
url_post = BASE_URL + 'posts'
url_comments = BASE_URL + 'comments'


response = requests.get(url_post)
if response.status_code == 200:
    print(response.status_code)
    # print(response.content)
#     parse response data
    json_data = json.loads(response.text)
    for post in json_data:
        print(post.get('title'),'\n')
else:
    print(response.status_code)
    print("not abel to fetch the comments")


