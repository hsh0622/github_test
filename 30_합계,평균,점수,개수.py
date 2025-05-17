total = 0
cnt = 0
while True:
    a = float(input("점수: "))
    print()
    if a == -1:
        break
    total += a
    cnt +=1

avg = total/cnt
print("="*9)
print()
print(f"합계: {total}")
print()
print(f"평균: {avg:.1f}")