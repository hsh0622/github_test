#42-1. 입력수까지 약수 오름차순 출력
a = int(input("자연수:"))
for i in range(1,a+1):
    if a%i == 0:
        print(i)

#42-2. 입력수까지 약수 내림차순 출력
b = int(input("자연수:"))
for i in range(b,0,-1):
    if b%i == 0:
        print(i)