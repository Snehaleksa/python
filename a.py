l=[]
a=int(input('Enter the number of elements: '))
for i in range(a):
    b=int(input(f'enter the number{i+1}:'))
    l.append(b)
c=int(input('enter the largest number to find: '))
f=sorted(l,reverse=True)[:c]
print(f)







                          
   
        



