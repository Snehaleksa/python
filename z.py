n=7
a=1
b=5
for i in range(0,7):
    for j in range(0,7):
        if i==0 or i==6:
            print('*',end=" ")
        elif i==a and j==b:
            print('*',end=' ')
            a=a+1
            b=b-1
        else:
            print(' ', end=' ')  
    print()  


    
                   

              



            
