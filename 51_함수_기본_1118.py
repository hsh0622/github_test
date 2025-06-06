# 51-1
def fun_s(n):
    s = 0
    for i in range(1,n+1):
        s += i
    return s
print(fun_s(10))

# 51-2
def fun_fact(n):
    a = 1
    for j in range(1,n+1):
        a *= j
    return a
print(fun_fact(5))
print(fun_fact(10))