l={}
while True:
    print('1.Create account \n'
          '2.Deposite\n'
          '3.Withdraw \n'
          '4.Delete Account')
    x=int(input('Enter the option :'))
    if x==1:
        a=int(input('Enter the account number :'))
        b=int(input('Enter the initial Amount :'))
        l[a]=b
        print('Succesfully account created')
    elif x==2:
        a=int(input('Enter the account number:'))
        amount=int(input('Enter the amount to deposit:'))
        l[a]=amount
        print('Succesfully amount deposited')
    elif x==3:
        a=int(input('Enter the account number:'))
        d=int(input('Enter the amount to withdrow:'))
        if a in l and d<(amount+b):
            l[a]=l[a]-d
            print('succussfully withdrow')         
        else:
            print('no')           
    elif x==4:
        break   
                    



            
