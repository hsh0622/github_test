import random

a = 1
b = 4
k = 2
step = 2
list = [1,2,3,4]

print(random.random()) #0 이상 1 미만 실수 랜덤 추출
print(random.uniform(a,b)) #a 이상 b 미만 실수 랜덤 추출
print(random.randint(a,b)) #a 이상 b 이하 정수 랜덤 추출
print(random.randrange(a,b,step)) #a 이상 b 미만 step 간격으로 생성된 정수 중 랜덤 추출
print(random.choice(list)) #리스트중에 하나
print(random.choices(list,k=2)) #리스트중에 k개
print(random.sample(list,k)) #리스트중에 k개(중복 안댐)
print(random.shuffle(list))