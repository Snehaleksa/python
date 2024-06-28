a=[1,2,3,1,8,7,8]
l=[]
newlist=[]
for i in a:
    if i not in l:
        l.append(i)   
    elif i not in newlist:
        newlist.append(i)
print(newlist)    