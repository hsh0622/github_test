import random



hap = 0

while True:
    a = random.randint(1,10)
    b = random.randint(1,10)
    start = min(a,b)
    end = max(a,b)
    print(f"{start}~{end}=>{hap}")
    if start == end:
        break
    else:
        for i in range(start,end+1):
            hap+=i