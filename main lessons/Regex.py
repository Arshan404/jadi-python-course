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

print("------------------")

import re

T = {
    "nasrin": "+91223034 1234-5678-9872-2341",
    "bita": "+9123039 @bitabita",
    "jadi": "+9031415 @jadijadi 6221-0610-1111-2222",
    "sina": "9876-9383-1234-4321"
}

all_text = " ".join(T.values())

# پیدا کردن اولین شماره که با + شروع میشه
match = re.search(r'\+\d+', all_text)
match2 = re.search(r'\d', all_text)

print(match)          # شیء Match
print(match2)         
print(match.group())  # شماره پیدا شده

# جستجو برای الگوی +عدد+
match3 = re.search(r'\+\d+\+', all_text)
print(match3)

print("------------------")

data = """
        "nasrin": "+91223034 1234-5678-9872-2341",
    "bita": "+9123039 @bitabita",
    "jadi": "+9031415 @jadijadi 6221-0610-1111-2222",
    "sina": "9876-9383-1234-4321" 
       """

import re

print(re.findall(r'\d+' , data))
print(re.findall(r"\+\d+" , data))                     #در اوردن شماره تلفن ها
print(re.findall(r"\d{4}-\d{4}-\d{4}-\d{4}" , data))   #در اوردن شماره کارتها
print(re.findall(r"(\d{4})-\d{4}-\d{4}-\d{4}" , data)) # در اوردن نام بانکها چون با استفاده از 4 رقم اول امکان پذیره پس گروه بندیشون میکنیم
matches = re.finditer(r"(\d{4})-\d{4}-\d{4}-\d{4}" , data)
for match in matches:
    print(matches)
    print(match.group())                                 # هرکدوم از پرینت ها که خواستی کار کنه اون یکی دیگه هارو کامنت کن
    print(match.group(1))                               #برخلاف پایتون که 0 اولیشه تو رجکس ها 1 یعنی اول


print(re.search(r'\@\w+' , data))                       #بهتر اینع که یک پترن شکل بدیم
pattern = re.compile(r'\@\w+')
print(re.search( pattern, data))
pattern2 = re.compile(r'\@(\w+)')
print(re.search( pattern2, data))


test = 'my name is @jadi_jadi in nowhere'
print(re.search(pattern2 , test))

test3 = 'my name is @jadi%jadi in nowhere'
pattern3 = re.compile(r'\@([\w%]+)')
print(re.search( pattern3, test3))

