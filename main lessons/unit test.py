def countc(s,c):
    found = 0
    for this_char in s:
        if this_char ==c:
            found +=1
    return found

print(countc("jadi jaan" , "a"))