s = set()
s.add(1)
s.add(2)
print(s)
s = {4,5,6}
print(s)
print(s.remove(5))
print(s)
#print(s.remove(100))   #ارور میده چون تو مجموعه 100 نداریم
print(s.discard(100))  #اگه 100 تو مجموعه باشه بیخیالش میشه ولی اگرم نباشه دیگه ارور نمیده
print(s.clear())
print(s)

s1 = {1,2,3}
s2 = s1
print(s2)
s1.add(100)
print(s1)
print(s2)

s11 = {1,2,3}
s12 = s11.copy()
s11.add(100)
s11.remove(2)
print(s11)
print(s12)

s15 = {3,4,5}
s16 = {5,7,8}
print(s15.isdisjoint(s16))
print(s15.intersection(s16))
print(s15.difference(s16))
s15.difference_update(s16)         #تفاوتش با بالایی اینه که تفاوت رو محاسبه میکنه و خودش رو با اون تفاوت ها اپدیت میکنه
print(s15)
