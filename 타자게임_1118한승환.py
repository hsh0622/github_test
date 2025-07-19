import random
import time

w = ["cat","dog","fox","monkey","mouse","panda","frog","snake","wolf"]

n = 0
cnt = 1

start = time.time()

while True:
    if n == 5:
        stop = time.time()
        print(stop-start)
        break
    else:
        print(f"[문제 {cnt}]")
        word = random.choice(w)
        print(word)
        user = input()
        if user == word:
            print("pass")
            print()
            n += 1
        else:
            print("fail")
            print()
    cnt += 1
