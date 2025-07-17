#تعریف مجموعه
myset = set()

#اضافه کردن به مجموعه
myset.add(1)
myset.add(2)

print(myset)

#مشخص کردن تایپ چیزی تعریف کردیم
print(type(myset))

chess = set()

chess.add("jadi")
chess.add("sarah")

sofal = set()
sofal.add("jadi")
sofal.add("hasan")

print(chess)
print(sofal)
print(sofal.union(chess)) # یعنی جمع دو مجموعه
print(sofal.intersection(chess)) #نقطه مشترک دو مجموعه

heyvoons = set(['sag' , 'dog' 'gorg' ,'fok']) # ساختن مجموعه مستقیما از لیست
print(heyvoons)