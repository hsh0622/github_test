import random
com = random.randint(1,20)
print("<<컴퓨터가 생각한 1~20 숫자 맞추기>>")
while True:
    user = int(input("숫자입력(종료:0)"))
    if user > com:
        print("더 작은 숫자 입력!")
    elif user < com:
        print("더 큰 숫자 입력!")
    elif user == com:
        print("정답!")
        break