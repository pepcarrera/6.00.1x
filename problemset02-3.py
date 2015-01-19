balance = 320000
annualInterestRate = .2



months = 12
testBalance = balance
low = balance/12
epsilon = .01


def balancePaid(payment):
    totBalance = balance
    for x in range(months):
        unpaidBalance = totBalance - payment
        totBalance = unpaidBalance + (annualInterestRate/12.0) * unpaidBalance
    return totBalance

high = (balancePaid(0)/12)
ans = (high + low)/2.0

while True:
    testBalance = balancePaid(ans)
    if abs(testBalance) <= epsilon:
        break
    elif testBalance < epsilon:
        high = ans
    else:
        low = ans
    ans = (high + low)/2.0

print('Lowest Payment: ' + str(round(ans,2)))





