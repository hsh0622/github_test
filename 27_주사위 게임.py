import random

first = random.randint(1,6)
second = random.randint(1,6)
Com = []
Com.append(first)
Com.append(second)

user_list = list(map(int,input("2개 입력(1~6, 중복 허용:").split()))
if user_list[0] == Com[0] and user_list[1] == Com[1] or user_list[1] == Com[0] and user_list[0] == Com[1]:
    print(f"Com={Com} User={user_list}")
    print("1등!")
elif user_list[0] == Com[0] or user_list[0] == Com[1] or user_list[1] == Com[0] or user_list[1] == Com[1]:
    print(f"Com={Com} User={user_list}")
    print("2등!")
else:
    print(f"Com={Com} User={user_list}")
    print("3등!")