a = int(input())
for i in range(1,a+1):
    for j in range(i):
        print("*",end="")
    print()

b = int(input())
for i in range(b,0,-1):
    for j in range(i):
        print("*",end="")
    print()

c = int(input())
for i in range(1,c+1):
    for j in range(c-i):
        print(" ",end="")
    for k in range(i):
        print("*",end="")
    print()

d = int(input())
for i in range(d,0,-1):
    for j in range(d-i):
        print(" ",end="")
    for k in range(i):
        print("*",end="")
    print()