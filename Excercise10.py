# ATM case: Ask user for balance and withdrawal amount → if withdrawal is possible, subtract and show balance, else print "Insufficient Funds".
balance = int(input("Enter your balance: "))
Withdrawal = int(input("Enter your Withdrawal amount: "))
if Withdrawal <= balance:
    balance -= Withdrawal
    print ("Your Withdrawal successful!, Your balance is", balance)
else:
    print ("insufficent funds")