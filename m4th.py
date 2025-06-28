import math

lst = list(range(1,11))

mean = sum(lst)/len(lst)
print(f"평균:{mean}")

vsum = 0
for x in lst:
    vsum = (x - mean)**2
var = vsum/len(lst)
print(f"분산:{var}")

std = math.sqrt(var) #std = var**1 (1/2)
print(f"표준편차:{std}")

gcd = math.gcd(*lst)
lcm = math.lcm(*lst)
print(f"최대공약수:{gcd} 최소공배수:{lcm}")

#가변길이 리스트를 인자로 사용할 때 *사용