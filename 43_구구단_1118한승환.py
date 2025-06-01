#43-1. 구구단(2 ~ 9단)
for i in range(1,10):
    print(f"=={i}단==")
    for j in range(1,10):
        print(f"{i} * {j} = {i*j}")

#43-2. 구구단(단 입력)
a = int(input("몇 단?"))
print(f"=={a}단==")
for i in range(1,10):
    print(f"{a} * {i} = {a*i}")