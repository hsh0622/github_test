print("#"*23)
print("  BMI 계산 프로그램  ")
print("#"*23)
a = int(input("키:"))
b = int(input("몸무게:"))
print("#"*23)
bmi = b/(a/100)**2
print(f"당신의 BMI 치수는 {bmi}입니다.")