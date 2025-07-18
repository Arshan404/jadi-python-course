n = 7
for i in range(n):
     print(" " * (n-i), end=" ")
     for j in range(i+1):
      if i % 2 == 0:
       print("*", end=" ")
      else:
       print(j+1, end=" ")
     print()
