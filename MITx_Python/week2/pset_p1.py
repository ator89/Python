"""# Test Case 1:
balance = 42
annualInterestRate = 0.2
monthlyPaymentRate = 0.04

# Result Your Code Should Generate Below:
Remaining balance: 31.38

To make sure you are doing calculation correctly, this is the
remaining balance you should be getting at each month for this example
    Month 1 Remaining balance: 40.99
    Month 2 Remaining balance: 40.01
    Month 3 Remaining balance: 39.05
    Month 4 Remaining balance: 38.11
    Month 5 Remaining balance: 37.2
    Month 6 Remaining balance: 36.3
    Month 7 Remaining balance: 35.43
    Month 8 Remaining balance: 34.58
    Month 9 Remaining balance: 33.75
    Month 10 Remaining balance: 32.94
    Month 11 Remaining balance: 32.15
    Month 12 Remaining balance: 31.38


Monthly interest rate= (Annual interest rate) / 12.0
Minimum monthly payment = (Minimum monthly payment rate) x (Previous balance)
Monthly unpaid balance = (Previous balance) - (Minimum monthly payment)
Updated balance each month = (Monthly unpaid balance) + (Monthly interest rate x Monthly unpaid balance)



balance = 4973.5
annualInterestRate = 0.18
monthlyPaymentRate = 0.02

monthlyInterestRate = annualInterestRate/12.0
minimumPayment = balance * monthlyPaymentRate
unpaidBalance = balance - minimumPayment
monthlyInterest = (annualInterestRate/12) * unpaidBalance
interest =(annualInterestRate/12) * unpaidBalance

nextBalance = unpaidBalance + (monthlyInterestRate*unpaidBalance)

print("\nRemaining balance:",balance)
print('Next Balance: ',nextBalance)
print("Monthly Interest:",monthlyInterest)
print('Minimum Payment:',minimumPayment)
print('Unpaid Balance:',unpaidBalance)
"""

balance = 42
annualInterestRate = 0.2
monthlyPaymentRate = 0.04

monthly_interest_rate = (annualInterestRate / 12)

for i in range(1, 13):
    # minimum that should be paid
    minimum_monthly_payment = round(monthlyPaymentRate * balance, 2)

    # deducts the min payment from balance
    monthly_unpaid_balance = round(balance - minimum_monthly_payment, 2)

    # adds interest fees
    balance = round((balance - minimum_monthly_payment) + (monthly_unpaid_balance * monthly_interest_rate), 2)

print('Remaining balance:',balance)
