import requests

response = requests.get("https://en.wikipedia.org/wiki/Python_(programming_language)")
#print(response)  
#print(type(response))
#print(response.status_code)
#print(response.url)
#print(response.text)

data = response.text
import bs4
soup = bs4.BeautifulSoup(data)
#print(soup)

sakhtar = bs4.BeautifulSoup(data)
print(sakhtar.select('title'))
t = sakhtar.select('title')
print(t)
print(t[0])
print(type(t[0]))
mytitle = t[0]
print(mytitle.getText())
print(mytitle.get_text())       #مرسوم تره
w = sakhtar.select('li')
#print(w)
print(len(w))
for item in sakhtar.select('li'):
    print(item.text)

all_toc = sakhtar.select('.vector-toc-text')
for toc in all_toc:
    print(toc.text)
