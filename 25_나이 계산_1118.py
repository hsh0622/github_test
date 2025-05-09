a,b = map(int,input().split(","))
year = (a//10000)
if b == 1 or b == 2:
    old_age = 100-year+26
    print(f"현재나이는 {old_age}살 입니다.")
elif b == 3 or b == 4:
    young_age = 26 - year
    print(f"현재나이는 {young_age}살 입니다.")
else:
    print("존재하지 않습니다.")