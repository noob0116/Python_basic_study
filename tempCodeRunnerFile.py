def deposit(balance, money): # 입금
    print("임금이 완료되었습니다. 잔액은 {0} 원입니다".format(balance + money))
    return balance + money

def withdraw(balance, money):
    if balance >= money: # 잔액이 출금보다 많으면
        print("출금이 완료되었습니다. 잔액은 {0} 원입니다.".format(balance - money))
        return balance - money
    else:
        print("출금에 실패하였습니다 잔액은 {0} 원입니다.".format(balance))
        return balance
def withdraw_night(balance, money): # 저녁에 출금
    commission = 100 # 수수료
    return commission, balance - money - commission # return 을 할때 , 를 이용해서 2개의 값을 반환할 수도 있다.


balance = 0 # 잔액
balance = deposit(balance, 10000)
balance = withdraw(balance, 500)
commission, balance = withdraw_night(balance, 200)
print("수수료 {0} 원이며, 잔액은 {1} 원입니다.".format(commission, balance))
