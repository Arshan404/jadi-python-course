class Book():
    book_type = 'horror'
    def __init__(self ,page):
        self.pages = page

    def open(self):
        print(f'opened the book on last page ({self.pages})')

b = Book(400)
print(b.pages)
print(b.open())
b1 = Book(340)
print(b1.book_type)
b2 = Book(500)
print(b2.book_type)
b1.book_type = 'fun'
Book.book_type  = 'triller'  #در واقع اینجا کلاس رو یکضرب عوض کردیم
b3 = Book(10)
print(b3.book_type)


print("-----------------------")

class circle():
    pi = 3.1415926
    def __init__(self , r):
        self.r = r
    def masahat(self):
        m = self.r * self.r * self.pi
        return m 
    
c1 = circle(10)
print(c1.masahat())
