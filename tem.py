a,b = map(int,input().split())

avg = []

for i in range(a):
    lst = list(map(int, input().split()))
    total = 0
    for j in lst:
        total += j
    avg.append(total / b)

for i in avg:
    print(i)