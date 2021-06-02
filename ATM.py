'''
crete a class ATM which has parameterised constructor
which takes two arguments card_no and Acc_balance. 
Then it has three functions:
1. Withdraw()-> takes amount as argument and withdraw the amount,
                if it is available.
2. deposit() -> takes amount as argument and add the given amount 
                in the Acc_balance if the entered amount is greater than 0.
3. getbalance() -> this method will print the current Acc_balance.
'''
class ATM:
    #parameterised constructor takes two argument and assign it to this class variables.
    def __init__(self, card_no, Acc_balance):
        self.card_no = card_no
        self.Acc_balance = Acc_balance
        
    # this method takes amount as argument and withdraw the amount if it is available in the Acc_balance.
    def withdraw(self,amount):
        if amount>self.Acc_balance:
            print("OOPS! Unable to withdraw amount, Low balance")
        else:
            self.Acc_balance -= amount
            print("Amount withdrawn")
        
    ''' this method takes the amount as the argument and deposit it in the current Acc_balance
        if the enterd amount is greater than 0 otherwise print the message as Invalid amount.
    '''
    def deposit(self,amount):
        if amount>0:
            self.Acc_balance += amount
            print("Amount Deposited")
        else:
            print("Invalid amount to deposit")
     
    # this method will return the current Acc_balance.        
    def getBalance(self):
        print(self.Acc_balance)
            
atm_acc_1 = ATM("1234", 400)
atm_acc_2 = ATM("10001", 100)

atm_acc_1.withdraw(300)
atm_acc_1.withdraw(300)
atm_acc_1.deposit(300)
atm_acc_1.getBalance()
atm_acc_2.getBalance()
atm_acc_2.deposit(300)
atm_acc_2.getBalance()

'''
Output:
    Amount withdrawn -> acc1 has Rs.400 in balance and rs.300 has withdrawn.
    OOPS! Unable to withdraw amount, Low balance ->Now the acc1 has 100 in its balance.
    Amount Deposited -> Now rs.300 is deposited in the acc1.
    400 -> the balance of the acc1.
    100 -> the balance of the acc2.
    Amount Deposited ->Now rs.300 is deposited in the acc2.
    400 -> The balance of the acc2.
'''

