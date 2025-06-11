#58-1
def sub1(x):
    a = x+100
    return 

def sub2(x):
    global a
    a = x+100
    return a

a = 10
print(sub1(a))
print(a)
print(sub2(a))
print(a)

58-2
def sub_1(lst):
    mylst = list(range(7,11))
    print(f'sub_1 함수 리스트: {mylst}')

def sub_2(lst):
    global mylst
    mylst = list(range(1,5))
    print(f'sub_2 함수 리스트: {mylst}')

mylst = list(range(10,50,10))
sub_1(mylst)
sub_2(mylst)
print(f'메인함수 리스트: {mylst}')