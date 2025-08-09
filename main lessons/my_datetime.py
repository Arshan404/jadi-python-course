import datetime

print(datetime.date(2025, 1, 1))  

nkh = datetime.date(2025,1,1)
print(nkh.day)
print(nkh.month)
print(nkh.weekday())
print(nkh.ctime())

datetime.datetime(1978,1,15,9)           #تاریخ و ساعت تولد جادی

jt = datetime.datetime(1978,1,15,9)
print(jt.weekday())


print(datetime.date.today())
print(datetime.datetime.now())
now = datetime.datetime.now()
print(now)

print(now-jt)

sen = now-jt
print(sen.days)

from datetime import datetime
print(datetime.now())
print(now.ctime())