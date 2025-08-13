s = 'jadi has a phone. its number is +9123989'
print('phone' in s )
print('+9123989' in s)
print(s.index('+9123989')) 

import re

print(re.search("jadi" , s))
print(re.search('shadi' , s))
print(re.search('adi' , s))

r = re.search('jadi' , s)
print(r)
print(r.start())
print(r.end())
print(r.group())
print(r.span())

s2 = 'jadi has a phone. its number is +9123989 and jadi is cool'
print(re.search('jadi' , s2))
print(re.findall('jadi' , s2))
for match in re.finditer('jadi' , s2):
    print(match)

print(re.search(r'\d' , s2))
print(re.findall(r'\d' , s2))
