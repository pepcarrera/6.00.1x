balance = 4213
annualInterestRate = .2
monthlyPaymentRate = .04

months = 12
totalPaid=0.0

for x in range(months):
    monthlyPayment = balance*monthlyPaymentRate
    unpaidBalance = balance-monthlyPayment
    balance = unpaidBalance + (annualInterestRate/12.0) * unpaidBalance
    totalPaid += monthlyPayment
    print('Month: ' + str(x+1))
    print('Minimum monthly payment: ' + str(round(monthlyPayment,2)))
    print('Remaining balance: ' + str(round(balance,2)))

print('Total paid: ' + str(round(totalPaid,2)))
print('Remaining balance: ' + str(round(balance,2)))