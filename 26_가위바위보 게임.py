import random
com = random.randint(1,3)
if com == 1:
    com = "가위"
elif com == 2:
    com = "바위"
elif com == 3:
    com = "보"
user = input("가위,바위,보 중에 하나 입력:")
if user == com:
    game = "비겼음"
elif user == "가위" and com == "보":
    game = "이겼음"
elif user == "바위" and com == "가위":
    game = "이겼음"
elif user == "보" and com == "바위":
    game = "이겼음"
elif user == "보" and "가위":
    game = "졌음"
elif user == "가위" and "바위":
    game = "졌음"
elif user == "바위" and "보":
    game = "졌음"
else:
    print("오타가 있는지 확인해주세요.")
print(f"user:{user},com:{com}->{game}")