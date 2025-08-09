import collections

from collections import Counter

mylist = [1,2,3,4,2,3,1,2]

print(Counter(mylist))

c = Counter(mylist)
print(c.get(2))

print(c.most_common())

from collections import namedtuple

Kelas = namedtuple('Kelas' , ['tedad' , 'avg' , 'ostad'])
print(Kelas)

fizik = Kelas(tedad=40 , avg=8.2 , ostad='jadi')
print(fizik)
print(fizik.tedad)
print(fizik[0])

a = dict()
a['name'] = 'jadi'
print(a)
print(a['name'])

from collections import defaultdict

d = defaultdict(lambda : 20)

d['name'] = 'jadi'
print(d)
print(d['family'])