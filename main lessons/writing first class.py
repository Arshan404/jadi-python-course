l = [3,4,5,]
print(type(l))
print(l.index(3))

n = 'jadi'
print(type(n))
print(n.count('a'))

class Test():
    pass

t = Test()
print(type(t))

class Book():
    def __init__(self , page):
        self.pages = page

mybook = Book(540)
yourbook = Book(14)
print(mybook.pages)
print(yourbook.pages)
print(type(mybook))