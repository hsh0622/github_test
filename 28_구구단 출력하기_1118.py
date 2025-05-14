a = int(input("단 입력:"))
print()
for i in range(1,10):
    print(f"{a} X {i} = {a*i}")
    if i != 9:
        print()