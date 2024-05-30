d = {}
while True:
    print('1 create account \n'
          '2.deposit  \n'
          '3.withdraw   \n'
           '4.delete')
    x = int(input("enter the choice :"))
    if x==1:
        a=(input('Account number'))
        b=(input('Enter amount'))
        l1={}
        l1.update({a:b})
        l1.update(b)
        d.update(l1)

    if x==2:
        while True:
            print('1.account number\n'
                  '2-amount')
            x=int(input("enter your choice "))
            if x==1:
                
