class Bank:
 def __init__(self):
  self.account={}
 def create_account(self,account_number,name,age,amount,address):
  if account_number in self.account:
    return 'Account alrady exist'
  else: 
   self.account[account_number]={
   'name':name,
   'age':age,
   'amount':amount,
   'address':address
  }
   return self.account
  
 def deposit(self,account_number,amount):
   if account_number  in self.account:
    self.account[account_number]['amount']+=amount
    return self.account
   else:
     print('Account doesnot exist')
 
   
 
  
 def withdrow(self,account_number,amount):
  if account_number not in self.account:
   return 'Account doesnot exist'
  if self.account[account_number]['amount']<amount:
     return 'insufficient balance'
  self.account[account_number]['amount'] -= amount
  return self.account
 print('Succesfully withdrow')
 def delete_account(self,account_number):
   if account_number not in self.account:
     return 'Account doesnot exist'
   if account_number in self.account:
     return 'Account deleted'
 def display(self):
  for account_number in self.account.values():
    print (f"AccountNumber:{account_number['account_number']}")
    print(f"Name:{account_number['name']}")
    print(f"Age:{account_number['age']}")
    print(f"Amount:{account_number['amount']}")
    print(f"Address:{account_number['address']}")
    print('  ')
    
      
  
bank=Bank()
while True:
   print('1.Create account \n'
          '2.Deposite\n'
          '3.Withdraw \n'
          '4.Delete account\n'
          '5.Display all accounts')
   x=int(input('Enter the option :'))
   if x==1:
    
    account_number=int(input('Enter the account number :'))
    name=input('Enter the  name :')
    age=int(input('enter age'))
    amount=int(input('enter the amount'))
    address=input('enter the address')
    results=bank.create_account(account_number,name,age,amount,address)
    print(results)
    
   elif x==2:
    account_number=int(input('Enter the Account number'))
    amount=int(input('Enter the amount to deposit'))
    results=bank.deposit(account_number,amount)
    print(results)
   elif x==3: 
    account_number=int(input('enter the account'))
    amount=int(input('enter the amount to withdrow'))
    results=bank.withdrow(account_number,amount)
    print(results) 
   elif x==4:
      account_number=int(input('Enter the account number'))
      results=bank.delete_account(account_number)
      print(results)
  



