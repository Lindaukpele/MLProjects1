
import random

class BankAccount:
    last_customer_id = 0   #Class variable to track the last customer ID
    last_account_number = 1000 #Class variable to track the last account number

    def __init__(self, customer_name, account_type, balance=0):
        BankAccount.last_customer_id +=1
        BankAccount.last_account_number +=1

        self.customer_id = BankAccount.last_customer_id 
        self.account_number = BankAccount.last_account_number
        self.customer_name = customer_name        
        self.account_type = account_type if account_type in ['checking', 'savings'] else 'checking'
        self.balance = balance 

        self.filename = f'{self.account_number} _{self.account_type}_{self.customer_name}.txt'

       
    def statementfile(self):
        print(f'Account Balance: {self.balance}')

        deposit_amount = int(input('Enter deposit amount: '))
        if deposit_amount > 0:
            self.balance += deposit_amount
            print(f'Your new balance after deposit: {self.balance}')
            
        withdrawal_amount = int(input('Enter withdrawal amount: '))
        if withdrawal_amount > 0 and withdrawal_amount <= self.balance:
            self.balance -= withdrawal_amount
            print(f"Withdrawal successful. Your new balance: {self.balance}")
            
        else: 
            print(f'Insufficient balance. Your balance is {self.balance}')
            input('withdrawal_amount:')
            print(f"Withdrawal successful. Your new balance: {self.balance}")


        return self.balance

#creating an instance of BankAccount
customer_1 = BankAccount('Linda', 'checking', 200)
customer_2 = BankAccount('James', 'savings', 150)
customer_3 = BankAccount('John', 'checking', 400)


customer_1.statementfile()
customer_2.statementfile()
customer_3.statementfile()

print(f"Customer_1: ID={customer_1.customer_id}, Account={customer_1.account_number}'), File={customer_1.filename}")
print(f"Customer_2: ID={customer_2.customer_id}, Account={customer_2.account_number}'), File={customer_2.filename}")
print(f"Customer_3: ID={customer_3.customer_id}, Account={customer_3.account_number}'), File={customer_3.filename}")



    

    