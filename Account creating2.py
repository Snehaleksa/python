class Bank:
    def __init__(self):
        self.accounts={}
def create(a,b):
    l[a]=b
    print('succesfully created')
def deposit(a,amount):
    l[a]=amount
    print('succesfully deposited')
def withdrow(a,d):
    if a in l and d<(amount+b):
        l[a]=l[a]-d
        print('succesfully withdrow') 
    else:
      print('Account not found')     
l={}
while True:
    print('1.Create account\n'
          '2.Deposite\n'
          '3.Withdraw \n'
          '4.Delete Account \n'
          '5.Display All Account')
    x=int(input('Enter the option :'))
    if x==1:
        a=int(input('Enter the account number :'))
        b=int(input('Enter the initial Amount :'))
        create(a,b)
    elif x==2:
        a=int(input('Enter the account number:'))
        amount=int(input('Enter the amount to deposit:'))
        deposit(a,amount)
    elif x==3:
        a=int(input('Enter the account number:'))
        d=int(input('Enter the amount to withdrow:'))
        withdrow(a,d)
    elif x==4:
        break 
    elif x==5:
        

