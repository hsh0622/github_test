a,b,c = map(int,input().split())
list = []
if a>=b and a>=c:
    if b>=c:
        list.append(a)
        list.append(b)
        list.append(c)
    else:
        list.append(a)
        list.append(c)
        list.append(b)
elif b>=a and b>=c:
    if a>=c:
        list.append(b)
        list.append(a)
        list.append(c)
    else:
        list.append(b)
        list.append(c)
        list.append(a)
elif c>=a and c>=b:
    if a>=b:
        list.append(c)
        list.append(a)
        list.append(b)
    else:
        list.append(c)
        list.append(b)
        list.append(a)
n = list[1]
print(f"두번째 수는 {n}입니다")