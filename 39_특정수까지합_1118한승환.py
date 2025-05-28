#39_1
a = int(input())
n = 0
for i in range(1,a+1):
    n += i
print(f"1부터 {a}까지의 합은 {n}")

#39_2
b = int(input("자연수 입력: "))
m = 1
for i in range(1,b+1):
    m *= i
print(f"{b}!은 {m}")