class Book():
    def __init__(self , name ,  page):
        self.pages = page
        self.name = name

    def open(self):
        print(f'opened the {self.name} which has {self.pages} pages')

    def __len__(self):
        return self.pages
    
    def __str__(self):
        r = f'{self.name}, {self.pages}'
        return r
    
    def __del__(self):
        print(f'oh the {self.name} book is vanishing !')


b1 = Book("c programming" , 234)
print(len(b1))
print(b1)
print(str(b1))
del b1