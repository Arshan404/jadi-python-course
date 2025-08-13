print(0.1 + 0.2 == 0.3)
print(0.1 +0.2)

from decimal import *

print(getcontext())

getcontext().prec = 3           #تغییردادن وضعیت اعشار

print(Decimal(1)/Decimal(3))
print(Decimal(0.1) + Decimal(0.2) ==Decimal(0.3))
print(Decimal('0.1') + Decimal('0.2') == Decimal('0.3'))     #تعیین دقیق مقدار اعشار

print(Decimal(3.14))
print(Decimal('3.14'))
print(Decimal('3.14') > 4)

print('1.2 2.3 4.5 6.8'.split())
print(map(Decimal , '1.2 2.3 4.5 6.8'.split()))
print(list(map(Decimal , '1.2 2.3 4.5 6.8'.split())))

data = list(map(Decimal , '1.2 2.3 4.5 6.8'.split()))
print(min(data))
print(max(data))
print(sum(data))
