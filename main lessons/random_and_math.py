import math

print(math.pi)
print(math.e)
print(math.inf)
print(99999<math.inf)
print(math.pow(5,2))
print(round(4.7))
print(math.floor(4.2))
print(math.ceil(4.7))
print(math.ceil(4.1))
print(round(4.5))
print(round(5.5))
print(math.log(100 , 10))
print(math.degrees(math.pi/2))
print(math.radians(90))

print("--------------")

import random

print(random.randint(1,6))
print(random.random())
 
numbers = range(10)
numbers = list(numbers)
print(numbers)
print("قبل از shuffle:", numbers)
random.shuffle(numbers)  # لیست رو درجا تغییر میده
print("بعد از shuffle:", numbers)


print(random.choices(numbers))
print(random.choices(['s' , 'k' , 'g']))
print(random.choices(['s' , 'k' , 'g'] , k=2))
print(random.sample(['s' , 'k' , 'g'] , k=2))


