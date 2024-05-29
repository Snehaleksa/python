a=[1,2,3,4,5,6,7]
b=0
c=[]
for i in a:
    b=i**2
    c.append(b)
print(c)   


string='pythonloop'
for s in string:
    if s=='o':
        print('if block')
else:
    print(s)  

print(range(15)) 
print(list(range(15))) 
print(list(range(2,10))) 
print(list(range(2,10,2)))

d=('Python','Java','Abc')
for i in range(len(d)):
    print(d[i].lower())


