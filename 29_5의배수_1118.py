while True:
    a = int(input("입력: "))
    if a==0:
        print("프로그램 종료")
        break
    elif a % 5 ==0:
        print("5의 배수 입니다.")
    elif a % 5!=0:
        print("5의 배수가 아닙니다.")