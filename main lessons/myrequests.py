import requests

response = requests.get("https://en.wikipedia.org/wiki/Python_(programming_language)")
print(response)  
print(type(response))
print(response.status_code)
print(response.url)
print(response.text)