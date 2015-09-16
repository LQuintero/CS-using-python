
balance = raw_input('Enter balance:')
annualInterestRate = raw_input('Enter annual interest rate:')
monthlyPaymentRate = raw_input('Enter monthly payment rate:')

month = 0
totalPaid = 0
while month < 12:
    month += 1
    #previousBalance = balance
    monthlyInterestRate = annualInterestRate / 12.0
    #minimumMonthlyPayment = monthlyPaymentRate * previousBalance
    minimumMonthlyPayment = monthlyPaymentRate * balance
    totalPaid = totalPaid + minimumMonthlyPayment
    #unpaidBalance = previousBalance - minimumMonthlyPayment
    balance = balance - minimumMonthlyPayment
    #updatedBalance = unpaidBalance + monthlyInterestRate * unpaidBalance
    balance = balance + monthlyInterestRate * balance
    print('Month: ' + str(month))
    print('Minimum monthly payment: ' + str(round(minimumMonthlyPayment,2)))
    print('Remaining balance: ' + str(round(balance,2)))
    print('Total paid: ' + str(round(totalPaid,2)))
    print('Remaining balance: ' + str(round(balance,2)))
