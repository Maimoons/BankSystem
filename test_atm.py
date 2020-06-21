from ATM import *


if __name__ == "__main__":
    print('Starting testing:',end='\n\n')

    print('Command: Create BankX',end='\n')
    print('Command: Open CustomerYs Savings account',end='\n')
    print('Command: Open CustomerYs Checkings account with $10',end='\n')
    print('Command: Set CustomerYs pin: 1244',end='\n')

    bankX = Bank('BankX')
    acc_numberY = bankX.createCustomer('CustomerY','Savings')
    bankX.getCustomer(acc_numberY).openCheckings(10)
    bankX.getCustomer(acc_numberY).setPin('1244')
    try:
        print('Command: Try setting same pin: 1244',end='\n')
        bankX.getCustomer(acc_numberY).setPin('1244')
    except Exception as e: print(e,end='\n\n')

    print('Command: Bank Teller Deposits $100 to CustomerYs Savings account',end='\n')
    print('Command: Bank Teller Withdraws $50 from CustomerYs Savings account',end='\n')
    bankX.getCustomer(acc_numberY).selectAccount('Savings').deposit(100)
    bankX.getCustomer(acc_numberY).selectAccount('Savings').withdraw(50)

    print('Command: Assert $50 in CustomerYs Savings account',end='\n')
    print('Command: Assert $10 in CustomerYs Checkings account',end='\n')
    assert(bankX.getCustomer(acc_numberY).selectAccount('Savings').checkBalance() == 50)
    assert(bankX.getCustomer(acc_numberY).selectAccount('Checkings').checkBalance() == 10)

    print('Command: Insert CustomerYs card',end='\n')
    print('Command: Enter Correct pin',end='\n')
    print('Command: Select Checkings Account',end='\n')
    print('Command: Check balance',end='\n')

    customerY = bankX.insertCard(acc_numberY)
    customerY.enterPin('1244')
    accountY = customerY.selectAccount('Checkings')
    print('Output:  Account balance $', accountY.checkBalance(),sep='',end='\n\n')


    print('Command: Open CustomerZs Checkings account',end='\n')
    acc_numberZ = bankX.createCustomer('CustomerZ','Checkings')
    try:
        print('Command: Try entering incorrect card',end='\n')
        customerZ = bankX.insertCard('1234')
    except Exception as e: print(e,end='\n\n')

    print('Command: Insert CustomerZs card',end='\n')
    customerZ = bankX.insertCard(acc_numberZ)
    
    try:
        print('Command: Try entering pin',end='\n')
        customerZ.enterPin('1111')
    except Exception as e: print(e,end='\n\n')

    try:
        print('Command: Try setting pin: abcd',end='\n')
        customerZ.setPin('abcd')
    except Exception as e: print(e,end='\n\n')

    print('Command: Set CustomerZs pin: 0336',end='\n')
    customerZ.setPin('0336')
    try:
        print('Command: Select Savings account',end='\n')
        accountZ = customerZ.selectAccount('Savings')
    except Exception as e: print(e,end='\n\n')

    print('Command: Select Checkings Account',end='\n')
    accountZ = customerZ.selectAccount('Checkings')

    try:
        print('Command: Try withdrawing $50',end='\n')
        accountZ.withdraw(50)
    except Exception as e: print(e,end='\n\n')

    print('Command: Deposit $50 in Checkings account',end='\n')
    print('Command: Withdraw $10 from Checkings account',end='\n')
    print('Command: Withdraw $40 from Checkings account',end='\n')
    print('Command: Assert $0 in CustomerYs Checkings account',end='\n')

    accountZ.deposit(50)
    accountZ.withdraw(10)
    accountZ.withdraw(40)
    assert(accountZ.checkBalance() == 0)
    
    try:
        print('Command: Withdraw $10 from Checkings account',end='\n')
        accountZ.withdraw(10)
    except Exception as e: print(e,end='\n\n')

    print('Command: Open CustomerZs Savings account with $100',end='\n')
    print('Command: Transfer $100 from Savings to Checkings',end='\n')
    print('Command: Assert $100 in CustomerYs Checkings account',end='\n')
    print('Command: Assert $0 in CustomerYs Savings account',end='\n')

    customerZ.openSavings(100)
    customerZ.transfer('Savings','Checkings',100)
    assert(accountZ.checkBalance() == 100)
    assert(customerZ.selectAccount('Savings').checkBalance() == 0)    





