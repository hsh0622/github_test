g = int(input())
if g<210 or g>=375:
    print("판정 불가")
elif 300<=g<375:
    print("특")
elif 250<=g<300:
    print("상")
elif 210<=g<250:
    print("보통")