<h1>README</h1>

Bank is a python implementation of a basic Bank System

</br>

<h2>Installation</h2>

Python 3

</br>

<h2>Usage</h2>

Clone Repository from GitHub

The project will consist of:

 1. ATM.py

 2. test\_atm.py

Note: test\_atm.py consists of sample test cases that can be run
</br></br>

>python3 test\_atm.py

To run custom test cases:

>python3

>from ATM import \*

> <call function>

</br>


<h2>Functions</h2>

Note: every function raises error for relevant incorrect input/output
</br>


<h3>Bank Functions</h3>

1. Initialize a new Bank

<pre>Example: Bank(&#39;bankName&#39;)</pre>
</br> </br>



2. Create a new customer in Bank

createCustomer(nameOfCustomer, typeOfAccount)

Returns account number of the created customer

<pre>Example: account_number = createCustomer(&#39;John&#39;, &#39;Savings&#39;)</pre>
</br></br>


3. Insert Card in ATM of bank

insertCard(account\_number)

<pre>Example: customer = insertCard(accountNumber)</pre>

Returns the customer of the card
</br></br>


<h3>Account Functions</h3>

4. Withdraw amount from account

withdraw(amount)

<pre>Example: account.withdraw(10)</pre>
</br></br>


5. Deposit amount in account

deposit(amount)

<pre>Example: account.deposit(10)</pre>
</br></br>


6. Check balance in account

<pre>Example: checkBalance()</pre>

Returns the balance in account
</br></br>


<h3>Customer Functions</h3>

7. Open a Savings account. Optional amount can be deposited

openSavings(amount)

<pre>Example: customer.openSavings(10)</pre>
</br></br>


8. Open a Checkings account. Optional amount can be deposited

openSavings(amount)

<pre>Example: customer.openCheckings(10)</pre>
</br></br>


9. Set a valid 4 digit pin for the customer

setPin(pin)

<pre>Example: customer.setPin(&#39;1234&#39;)</pre>
</br></br>


10. Enter a valid 4 digit pin for the customer

enterPin(pin)

<pre>Example: customer.enterPin(&#39;1234&#39;)</pre>
</br></br>


11. Select either a &#39;Savings&#39; or &#39;Checkings&#39; account of the customer

selectAccount(accountType)

<pre>Example: account = customer.selectAccount(&#39;Savings&#39;)</pre>

Returns the relevant account
</br></br>


12. Transfer money from one account type to another

transfer(fromType,toType,amount)

<pre>Example: customer.transfer(&#39;Savings&#39;,&#39;Checkings&#39;,10)</pre>
