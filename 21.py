cm = int(input("키(cm): "))
kg = int(input("체중(kg): "))
print("#"*10)
if cm>=130 and 25<=kg<100:
    print("이용 가능")
else:
    print("이용 불가능")