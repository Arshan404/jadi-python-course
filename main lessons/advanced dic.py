d = {'name' : 'jadi' , 'sen' : 42 , 9 : 47} #دیکشنری حتما لازم نیست کلیداش حتما رشته باشه
print(d)
print(d[9])

print([x*2 for x in [1,2,3]])
print({x: x*2 for x in [1,2,3]})            #برای تبدیل به دیکشنری جدای از کرلی براکت باید کلید و مقدار رو هم تعریف کنی
print({f"k{x}": x*2 for x in [1,2,3]})       #اینجوریم میشه ولی خیلی کار مرسومی نیست
print({f"k{x}": x*2 for x in range(10)}) 
print({k:v for k,v in zip(['a' , 'b'] , [0 , 1])})
my_dict = {k:v for k,v in zip(['a' , 'b' , 'c' , 'd'] , range(4))}
print(my_dict)
print(my_dict.values())
print(my_dict.keys())
print(my_dict.items())

for a in my_dict.items():
    print(a)

for k,v in my_dict.items():                   #کار مرسوم تریه
    print(k,v)


