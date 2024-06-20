class Main:
    def mul(self):
        a=int(input('Enter a number'))
        b=int(input('enter the limit'))
        for i in range(1,b):
          print(a,'x',i,'=',a*i)

obj=Main()
obj.mul()
        