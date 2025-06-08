import random

def genPass():
    chr = "abcdefghijklmnopqrstuvwxyz0123456789"
    password = ""
    for i in range(8):
        password += random.choice(chr)
    return password

for i in range(3):
    result = genPass()
    print(f"암호 {i+1}: {result}")