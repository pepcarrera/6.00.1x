balance = 3329
annualInterestRate = .2


ans = 0
months = 12
testBalance = balance

def balancePaid(payment):
    totBalance = balance
    for x in range(months):
        unpaidBalance = totBalance - payment
        totBalance = unpaidBalance + (annualInterestRate/12.0) * unpaidBalance
    return totBalance

while True:
    testBalance = balancePaid(ans)
    if testBalance <= 0:
        break
    else:
        ans += 10
print('Lowest Payment: ' + str(ans))