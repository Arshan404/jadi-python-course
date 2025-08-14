from PIL import Image

# مسیر کامل تصویر
file_path = r"D:\wallpapers\1704976240052.jpg"

# باز کردن و نمایش تصویر
img = Image.open(file_path)
#img.show()
print(img.info)
print(type(img))
print(img.size)
print(img.filename)
print(img.format)
print(img.mode)
unfixed  = img.rotate(90)
#unfixed.show()
u = img.crop((0, 200, 630, 430))  # left=0, top=200, right=630, bottom=430
# نمایش تصویر کراپ شده
#u.show()
#img.paste(u , (0,0))
#img.show()
print(img.getpixel((100,100)))    #based on RGB
#img.putpixel((100,100) , (255,0,0))
#img.show()
'''
for i in range(10):
    for j in range(10):
        img.putpixel((100+i,100+j) , (0,0,250))
'''        
#img.show()
for i in range(10):
    for j in range(10):
        img.putpixel((100+i, 100+j), (i*10, j*10, 0))  # اضافه کردن کانال B

#img.show()
#img.putalpha(30)
#img.show()

