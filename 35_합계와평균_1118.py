hap = 0
cnt = 0
while True:
    try:
        a = int(input("점수: "))
        hap += a
        cnt += 1
    except:
        avg = hap/cnt
        print("==========")
        print(f"합계: {hap:.1f}")
        print(f"평균: {avg:.1f}")
        break