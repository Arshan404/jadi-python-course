def countc(s,c):
    found = 0
    for i in range(len(s)):
        if s[i] ==c:
            found +=1
    return found

print(countc("jadi jaan" , "a"))