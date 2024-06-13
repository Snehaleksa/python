def add(num,name,price,wheel):
    l1=[]
    l1.append(num)
    l1.append(name)
    l1.append(price)
    l1.append(wheel)
    l.append(l1)
    print(l)
def a(x):
            x=int(input("enter your choice "))
            if x==1:

              for i in l:
                if i[3]==2:
                 print(i)
            elif x==2:
              for i in l:
                if i[3]==3:
                    print(i)
            elif x==3:
               for i in l:
                if i[3]==4:
                    print(i)
                else:
                   break                    
        
l=[]

while True:
    print("1-add vehicle\n"
          "2-display")
    x=int(input("enter your choice "))
    if x==1:
        num= int(input("enter the vehicle number "))
        name=input("enter vehicle name ")
        price=int(input("enter the price of vehicle "))

        wheel=int(input("enter number of wheels "))
        add(num,name,price,wheel)
    if x==2:
        while True:
            print("1-two wheeler\n"
                  "2-three wheeler\n"
                  "3-four wheeler")
            a(x)