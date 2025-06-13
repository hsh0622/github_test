class BankAccount:
    def __init__(self, acnt):
        self.acnt = acnt
        self.balance = 0

    def deposit(self, amt):
        print(f"['{self.acnt}']통장에 {amt}원이 입금됨.")
        self.balance += amt
        print(f"현재 잔액은 {self.balance}원\n")
        return self.balance
    
    def withdraw(self, amt):
        print(f"['{self.acnt}']통장에서 {amt}원이 출금됨.")
        self.balance -= amt
        print(f"현재 잔액은 {self.balance}원\n")
        return self.balance
    
    def check(self):
        print(f"['{self.acnt}'] 현재 잔액은 {self.balance}원\n")

    def transfer(self,target,amt):
        if amt>self.balance:
            print("잔액이 부족합니다.")
        else:
            target.balance += amt
            self.balance -= amt
            print(f"[{self.acnt}]님이 [{target.acnt}]님께 {amt}를 이체하였습니다.")
            print(f"[{target.acnt}의 잔액 {target.balance}]")

a = BankAccount("123-456")
a.deposit(10000)
a.withdraw(5000)

b = BankAccount("456-789")
b.deposit(2000)

a.check()
a.transfer(b,100)
a.check()