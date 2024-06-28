a=[]
n= int(input("Enter how many number : "))
for i in range(n):
    b = input(f"Enter the {i+1} number : ")
    c = []
    c.append(b)
    for x in b:
        a.append(int(x))
sum = sum(a)
l = []
for i in a:
   l.append(sum - i)
print(l)



