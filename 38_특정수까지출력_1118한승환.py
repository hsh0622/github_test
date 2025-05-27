#38_1
a = int(input("어디까지 출력할까요?:"))
for i in range(1,a+1):
    print(i)

#38_2
b = int(input("어디부터 출력할까요?:"))
for i in range(b,-1,-1):
    print(i)

#38_3
c = int(input("몇 단?:"))
print()
print(f"==={c}단===")
for i in range(1,10):
    print(f"{c} * {i} = {c*i}")