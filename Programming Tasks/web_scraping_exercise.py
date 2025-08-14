import requests
from bs4 import BeautifulSoup

url = "https://taaghche.com/"
Response = requests.get("https://taaghche.com/")

if Response.status_code == 200 :
    html_content = Response.text
else:
    print("Error fetching the website : " , Response.status_code)
    exit()

soup = BeautifulSoup(html_content , "html.parser")

page_title = soup.title.text
print("page Title : " , page_title)

book_elements = soup.find_all(class_ = "bookHeader_bookTitleContainer__7Z98p")
book_titles = [book.h3.a["title"] for book in book_elements]
print("\nBook Titles : ")
for title in book_titles:
    print("-" , title)

book_images = [book.find("img")["src"] for book in book_elements]
book_images = ["https://img.taaghche.com/audioCover/223292.jpg?w=150" + img for img in book_images]
print("\nBook Image Links : ")
for img in book_images:
    print("-" , img)