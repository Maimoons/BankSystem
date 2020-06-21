import re,numpy,random, string


class Bank():
    """The Bank class for the ATM system

    Attributes
    ----------
    name : str
        The name of the bank
    customers : dictionary[account_number: int] = account : obj
        The customers in the bank

    """
    
    def __init__(self,name):
        
        """Creates a Bank object with name and empty list of customers
        and a list of valid account types

        Parameters
        ----------
        name : str
            The name of the bank
        """
        self.name = name
        self.customers = {}
        self.account_types = ['Checkings','Savings']


    def getCustomer(self,account_number):
        """Getter for a customer

        Parameters
        ----------
        account_number : str
            The account number of the customer needed
        """
        return self.customers[account_number]
    
    def insertCard(self,account_number):
        """
        Parameters
        ----------
        account_number : str
            The account number of the customer

        Returns
        -------
        Account obj
            Returns the Account object for the given account number
            Raises Error if account number does not exist
        """
        if (account_number not in self.customers):
            raise ValueError("Error: Customer does not exist")
            
        return self.getCustomer(account_number)

    def _generateAccNumber(self):
        """
        Returns
        -------
        int
            Returns a new account number in the bank
        """
        number = ''.join(random.choices(string.digits, k=10))
        while (number in self.customers.keys()):
            number = ''.join(random.choices(string.digits, k=10))
            
        return number

    def createCustomer(self,name,acc_typ):
        """Creates a new customer in the bank 
           with the specified account type

        Parameters
        ----------
        name : str
            The name of the customer
        acc_typ: str
            The first account type for the new customer
        
        Returns
        -------
        str
            Returns the account number generated for the customer
            Raises Error if invalid account type is entered
        """
        if (acc_typ not in self.account_types):
            raise ValueError("Error: Account type does not exist")
            
        account_number = self._generateAccNumber()
        customer = Customer(name,account_number)
        
        if acc_typ == 'Savings':
            customer.openSavings()
        else: # account_typ == 'Checkings'
            customer.openCheckings()
            
        self.customers[account_number] = customer
        return account_number



    
        
    
class Account(object):
    """Parent class: The generic Account class for the Customer

    Attributes
    ----------
    account_number : str
        The account number for the bank
    balance : int
        The balance in the account
    """
    

    def __init__(self,account_number, amount = 0):
        """Creates an Account object with name and list of customers

        Parameters
        ----------
        account_number : str
            The account number for the bank
        balance : int
            The balance in the account
        """
        self.account_number = account_number
        self.balance = amount

    def withdraw(self,amount):
        """Withdraws money from the account

        Parameters
        ----------
        amount : int
            The amount to be withdrawn from the account
        
        Raises Error if incorrect amount or insufficient funds
        """
        
        if amount <= 0:
            raise ValueError("Error: Incorrect amount")

        if amount > self.balance:
            raise ValueError("Error: Insufficient funds")

        self.balance -= amount
          

    def deposit(self,amount):
        """Deposits money in the account

        Parameters
        ----------
        amount : int
            The amount to be deposited in the account

        Raises error if incorrect amount is entered
        """
        
        if amount < 0:
            raise ValueError("Error: Incorrect amount")
        self.balance += amount


    def checkBalance(self):
        """
        Returns
        -------
        int
            Returns the balance in the account
        """
        return self.balance
        
            


class SavingsAccount(Account):
    """Child Class: The Saving Account class
        Will include methods specific to Saving Account

    Attributes
    ----------
    type : str
        The saving account type
    apr : int
        The apr incurred on savings
    """
    
    def __init__(self,account_number, amount = 0, apr = 0.0, ):
        """Creates a Savings Account

        Parameters
        ----------
        account_number : str
            The account_number at the bank
        amount : int, optional
            The initial amount to be put in bank
        apr : int, optional
            The apr set on the account
        """
        super(SavingsAccount, self).__init__(account_number, amount)
        self.type = 'Savings'
        self.apr = apr

    def setApr(self,apr):
        """Sets apr on account

        Parameters
        ----------
        apr : int
            The apr set on the account
        """
        self.apr = apr
        
    

class CheckingsAccount(Account):
    """Child Class: The Checkings Account class
        Will include methods specific to Checkings Account

    Attributes
    ----------
    type : str
        The checking account type
    fee : int
        The fee incurred for maintenance
    """
    
    def __init__(self,account_number, amount = 0,fee=0):
        """Creates a Checkings Account

        Parameters
        ----------
        account_number : str
            The account_number at the bank
        amount : int, optional
            The initial amount to be put in bank
        fee : int, optional
            The fee incurred for maintenance
        """
        super(CheckingsAccount, self).__init__(account_number, amount)
        self.type = 'Checkings'
        self.fee = fee

    def setFee(self,fee):
        """Sets fee on account

        Parameters
        ----------
        fee : int
            The fee set on the account
        """
        self.fee = fee



class Customer():
    """The Customer class for customers in Bank

    Attributes
    ----------
    name : str
        The name of the customer
    account_number : str
        The account number of the customer
    accounts: dict[type] = acc : obj
        The dictionary of accounts of the customer
    pin : int
        The pin used by the customer
    """
    
    def __init__(self,name,account_number,pin = '0000'):
        """Creates a Savings Account

        Parameters
        ----------
        name : str
            The name of the customer
        account_number : str
            The account number of the customer
        pin : int, optional
            The 4 digit pin used by the customer
        """
        self.name = name
        self.account_number = account_number
        self.accounts = {}
        self.pin = pin

    def openSavings(self,amount=0):
        """Creates a Savings Account

        Parameters
        ----------
        amount : int, optional
            The amount to be put in the account
        
        Raises Error if account already exists
        """
        if ('Savings' in self.accounts):
            raise ValueError("Error: Savings account exists")
        
        self.accounts['Savings'] = SavingsAccount(self.account_number,amount)

    def openCheckings(self, amount=0):
        """Creates a Checkings Account

        Parameters
        ----------
        amount : int, optional
            The amount to be put in the account
        
        Raises Error if account already exists
        """
        if ('Checkings' in self.accounts):
            raise ValueError("Error: Checkings account exists")
            
        self.accounts['Checkings'] = CheckingsAccount(self.account_number,amount)

    
    def _validatePin(self,pin):
        """
        Private: Validates that PIN is a 4 digit number and not default 0000

        Parameters
        ----------
        pin : int
            The pin number to be validated

        Returns
        -------
        bool
            Return True if valid pin number, false otherwose
        """
        if (bool(re.match("\d{4}",pin)) and pin!='0000'):
            return True

        return False
    

    def setPin(self,pin):
        """
        Sets a valid PIN

        Parameters
        ----------
        pin : int
            The pin number to be validated

        Raises Error if invalid PIN or old PIN is entered
        """
        if (pin==self.pin):
            raise ValueError("Error: Enter a new PIN")

        if (not self._validatePin(pin)):
            raise ValueError("Error: Invalid PIN")

        self.pin = pin
                  
            
    def enterPin(self,pin):
        """
        Checks if entered PIN matched with account PIN

        Parameters
        ----------
        pin : int
            The pin entered

        Raises Error if PIN not set or invalid PIN is entered
        """
        if self.pin == '0000':
            raise ValueError("Error: Set PIN first")
        
        if pin != self.pin:
            raise ValueError("Error: Invalid PIN")

        return True
    

    def selectAccount(self,acc_typ):
        """
        Getter for the account of the Customer

        Parameters
        ----------
        acc_typ : str
            The account type to ge returned

        Returns
        ----------
            Account obj

        Raises Error if account type does not exist
        """
        if (acc_typ not in self.accounts):
            raise ValueError("Error: Account type does not exist")
        
        return self.accounts[acc_typ]


    def transfer(self,from_typ,to_typ,amount):
        """
        Transfers money from one account type to another

        Parameters
        ----------
        from_typ : str
            The account type to transfer from
        to_typ : str
            The account type to transfer to

        Raises Error if account type does not exist or insufficient funds
        """
        
        if (from_typ not in self.accounts or to_typ not in self.accounts):
            raise ValueError("Error: Account does not exist")

        from_acc = self.accounts[from_typ]
        to_acc = self.accounts[to_typ]
        
        if from_acc.checkBalance() < amount:
            raise ValueError("Error: Insufficient funds")

        from_acc.withdraw(amount)
        to_acc.deposit(amount)





            
            
            
            
            
