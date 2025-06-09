def get_data():
    a1, b1 = map(int,input("(x1, y1)").split(','))
    a2, b2 = map(int,input("(x2, y2)").split(','))
    return a1, b1, a2, b2

def get_line(a1, b1, a2, b2):
    if a1 == a2:
        rst = f'y = {a1}x'
    else:
        slp = (x2-x1) / (y2-y1)
        y_i = y1-slp*x1
        rst = f'y = {slp}x + {y_i}'
    return rst

x1, y1, x2, y2 = get_data()
line = get_line(x1, y1, x2, y2)
print(line)