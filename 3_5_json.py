import requests

url = "https://jsonplaceholder.typicode.com/todos/"
response = requests.get(url=url)
text = response.text
json = response.json()
print(type(text), type(json))

response = requests.get(url='http://httpbin.org/')
print(response.text)
print(response.json())