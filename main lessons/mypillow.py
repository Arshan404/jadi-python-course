from PIL import Image

# مسیر کامل تصویر
file_path = r"D:\wallpapers\1704976240052.jpg"

# باز کردن و نمایش تصویر
img = Image.open(file_path)
img.show()
print(img.info)
print(type(img))
print(img.size)
print(img.filename)
print(img.format)
print(img.mode)