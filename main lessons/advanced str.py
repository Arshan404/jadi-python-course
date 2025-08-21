s = 'jadi is here'
print(s.upper())      #همه حروف را بزرگ میکند
print(s.capitalize())  #فقط حرف اول را بزرگ میکند
print(s.title())        #حروف اول هر کلمه را بزرگ میکند
print(s.lower())
print(s.count('i'))
print(s.find('i'))      #مکان و ایندکس رو برمیگردونه
print(s.find('1'))      #دقت کن صفر برنمیگرونه هاااا
print(s.center(50 , '*'))
print(s.isalnum())
print(s.startswith('jadi'))
print(s.endswith('here'))
print(s.split())
print(s.split('i'))       #داره بر اساس i میبره
print(s.partition('i'))
my_list = ['jadi' , 'bita' , 'rozhina']
print(','.join(my_list))                       #اگه بخوایی با کاما اینهارو بهم بچسبونی خیلی کار راحتی نیست و حتی با نوشتن لوپ هم یک کامای اضافه میاد اخر رشته ولی با این کار از شر اون خلاص میشیم