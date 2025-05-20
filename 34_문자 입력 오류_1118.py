while True:
    print("##예외 처리 1##")
    try:
        n_1 = int(input("숫자: "))
    except ValueError:
        print("숫자만 입력하세요.")
    else:
        print(n_1)
        break