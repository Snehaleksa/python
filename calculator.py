class Calculator:
    def __init__(self,a,b):
        self.a=a
        self.b=b
    def add(self):
        return self.a+self.b
    def sub(self):
        return self.a-self.b
    def mul(self):
       return self.a*self.b
    def div(self):
       return self.a/self.b
while True:
    print('1.Add')
    print('2.sub')
    print('3.mul')
    print('4.div')
    print('5.Exit')
    choice=int(input('enter your choice:'))
    a=int(input('Enter a:'))
    b=int(input('enter b:'))  
    obj=Calculator(a,b)
    if choice==1:

       print(obj.add())
    elif choice==2:
        print(obj.sub())
        
    elif choice==3:
        print(obj.mul())
        
    elif choice==4:
        print(obj.div())
        
    elif choice==5:
        break
    else:
        print('invalid choice.Please try again')        




