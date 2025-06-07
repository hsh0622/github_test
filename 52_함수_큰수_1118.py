def maxp(a,b):
    if a>b:
        return a
    else:
        return b


a,b = map(int,input().split())
print(f"큰 수: {maxp(a,b)}")