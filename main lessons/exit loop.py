for a in [1,2,3]:
    pass

print("started")
for b in [1,2,3,4,5,6]:
    if b == 3:
        break
    print(b)
print("ended")

for c in [1,2,3,4,5,6]:
    if c == 3:
        continue
    print(c)
print("end of the loop")

n = 0
while n<20:
    n+=1
    if n % 3 == 0 and n % 5 == 0 :     #اول بررسی میکنیم که آیا عدد هم به 3 بخش پذیره و هم به 5 اگه نبود ادامه میده حلقه رو .اگه این دستور رو انتها مینوشتیم هیچ وقت به اجراش نمیرسید چون تمام جایگاه ها گرفته شده بودن
        print("hiphop")
        continue
    if n % 3 ==0:
        print("hop")
        continue
    if n % 5 ==0:
        print("hip")
        continue
    
    print(n)
