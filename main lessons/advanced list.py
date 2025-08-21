l = [1,2,3]
l.append(5)
print(l)
l.append(5)
l.append(5)
l.append(5)
print(l)
print(l.count(5))
l.insert(2,'jadi')
print(l)
print(l.pop())      #اخرین جز از لیست رو میکشه بیرون وتحویل میده
l.remove(1)
print(l)
l.remove(5)         #اولین 5 رو میگیره حذف میکنه
print(l)

q = [1,2,3,4]
n = q.pop()
print(n)

q.pop(1)
print(q)