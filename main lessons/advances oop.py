class Book():
    def __init__(self , name ,  page):
        self.pages = page
        self.name = name

    def open(self):
        print(f'opened the {self.name} which has {self.pages} pages')

b1 = Book("c programming" , 234)
b1.open()

class Darsi(Book):          #یک کلاس دارم به اسم درسی که به ارث برده هر انچه بوک دارد رو
    def __init__(self, reshteh , paye , name , pages):
        Book.__init__(self,name,pages)
        print("a new darsi book")
        self.reshteh = reshteh
        self.paye = paye
    def open(self):
        print(f"opened {self.name} of {self.reshteh} paye {self.paye}")

d = Darsi("tajrobi" , 3 ,  '300 nokteh' , 120 )
print(d.pages)
print(d.paye)
print(d.reshteh)
d.open()


class Runner():
    def __init__(self , name):
        self.name = name
    def action(self):
        print(f"{self.name} is running")

sarah = Runner('sarah')
sarah.action()

class cycling():
    def __init__(self , name):
        self.name = name
    def action(self):
        print(f"{self.name} is biking")

jadi = cycling("jadi mirmirani")
jadi.action()

for person in[sarah , jadi ]:
    person.action()

def show_waht_doing(ddd):
    ddd.action()

show_waht_doing(jadi)
show_waht_doing(sarah)

class Human():
    def __init__(self , name):
        pass
    def jump(self):
        raise NotImplementedError("implmeent the jump")
    
class programmer(Human):
    pass
    def jump(self):
        print("I jumped")
jadi = programmer('jadi')
jadi.jump()

