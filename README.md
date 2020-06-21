**README**

Bank is a python implementation of a basic Bank System

</br>

**Installation**

Python 3

</br>

**Usage**

Clone Repository from GitHub

The project will consist of:

ATM.py

test\_atm.py

Note: atm\_test.py consists of sample test cases that can be run

>python3 test\_atm.py

To run custom test cases:

>python3

>from ATM import \*

> <call function>

</br>


**Functions**

Note: every function raises error for relevant incorrect input/output
</br>


**Bank Functions**

1. Initialize a new Bank

Example: Bank(&#39;bankName&#39;)
</br> </br>



2. Create a new customer in Bank

createCustomer(nameOfCustomer, typeOfAccount)

Returns account number of the created customer

Example: account\_number = createCustomer(&#39;John&#39;, &#39;Savings&#39;)
</br></br>


3. Insert Card in ATM of bank

insertCard(account\_number)

Example: customer = insertCard(accountNumber)

Returns the customer of the card
</br></br>


**Account Functions**

4. Withdraw amount from account

withdraw(amount)

Example: account.withdraw(10)
</br></br>


5. Deposit amount in account

deposit(amount)

Example: account.deposit(10)
</br></br>


6. Check balance in account

Example: checkBalance()

Returns the balance in account
</br></br>


**Customer Functions**

7. Open a Savings account. Optional amount can be deposited

openSavings(amount)

Example: customer.openSavings(10)
</br></br>


8. Open a Checkings account. Optional amount can be deposited

openSavings(amount)

Example: customer.openCheckings(10)
</br></br>


9. Set a valid 4 digit pin for the customer

setPin(pin)

Example: customer.setPin(&#39;1234&#39;)
</br></br>


10. Enter a valid 4 digit pin for the customer

enterPin(pin)

Example: customer.enterPin(&#39;1234&#39;)
</br></br>


11. Select either a &#39;Savings&#39; or &#39;Checkings&#39; account of the customer

selectAccount(accountType)

Example: account = customer.selectAccount(&#39;Savings&#39;)

Returns the relevant account
</br></br>


12. Transfer money from one account type to another

transfer(fromType,toType,amount)

Example: customer.transfer(&#39;Savings&#39;,&#39;Checkings&#39;,10)
