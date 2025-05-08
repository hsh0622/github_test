print("1.삼각형 2.사각형 3.원")
a = int(input("도형종류: "))
if a == 1:
    width = float(input("밑변(cm): "))
    height = float(input("높이(cm): "))
    area = width*height/2
elif a == 2:
    width = float(input("밑변(cm): "))
    height = float(input("높이(cm): "))
    area = width*height
elif a == 3:
    r = float(input("반지름(cm): "))
    area = r*r*3.14
print(f"삼각형의 넓이는 {area}cm^2입니다.")