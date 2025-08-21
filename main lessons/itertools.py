import itertools
import itertools as it                #اسمش بلنده مخففش کردیم

a = it.cycle([1,2,3])
print(next(a))
print(next(a))
print(next(a))

nums = [1,2,3,4]
print(list(it.combinations(nums , 2)))  #تمام ترکیبات دوتایی روی لیستمون
print(list(it.combinations_with_replacement(nums , 2)))    #با جایگذاری
counter = it.count(3,10)
print(next(counter))
print(next(counter))
print(next(counter))
print(next(counter))

nums = [1,2,3,4]
it.accumulate(nums)
print(list(it.accumulate(nums)))

nums = [1,2,3,4]
khals = ['del' , 'gishniz' , 'khesht']
print(list(it.product(nums , khals)))
for n , kh in it.product(nums , khals):
    print(f"{n} {kh}")

