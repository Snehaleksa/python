
a=1
b=3
c=1
d=5
for i in range(0,5):
    for j in range(0,9):
        if i==0 and j==4:
            print('*',end=' ')    
        elif i==a and j==b:
            print('*',end=' ')
            a=a+1
            b=b-1
        elif i==c and j==d:
            c=c+1
            d=d+1
            print('*',end=' ')     
        else:
            print(' ',end=' ')
    print()  
e=1
f=2
g=1
h=6
for i in range(0,4):
    for j in range(0,8):
        if i==0 and j==1:
            print('*',end=' ')
        elif i==e and j==f:
            print('*',end=' ')
            e=e+1
            f=f+1
        elif i==0 and j==7:
            print('*',end=' ')     
        elif i==g and j==h: 
            print('*',end=' ') 
            g=g+1
            h=h-1  

        else:
            print(' ',end=' ')  

    print()           


   


     


                            






        


                 