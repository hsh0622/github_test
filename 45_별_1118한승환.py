#45-1
a = int(input("행 수:"))
for i in range(a+1):
    for j in range(i):
        print("*",end=" ")
    print()

#45-2
b = int(input("행 수:"))
for i in range(a,0,-1):
    for j in range(i):
        print("*",end=" ")
    print()

#45-3
c = int(input("행 수:"))
for i in range(1,c+1):
    for j in range(c-i):
        print(" ",end=" ")
    for k in range(i):
        print("*",end=" ")
    print()

#45-4
d = int(input("행 수:"))
for i in range(d):
    for j in range(i):
        print(" ",end=" ")
    for k in range(d-i):
        print("*",end=" ")
    print()

#45-5
e = int(input("행 수:"))
for i in range(1, e+1):
    for j in range(e-i):
        print(" ",end=" ")
    for k in range(2*i-1):
        print("*",end=" ")
    print()

#45-6
n = int(input("행 수(홀수):"))
m = int(n/2)+1
for i in range(1,m+1):
    for j in range(m-i):
        print(" ",end=" ")
    for k in range(2*i-1):
        print("*",end=" ")
    print()
for i in range(m-1,0,-1):
    for j in range(m-i):
        print(" ",end=" ")
    for k in range(2*i-1):
        print("*",end=" ")
    print()