def a(b):
    return [b]
list1=[1,5,8,4,2]
list1.sort(key=a)
list2=[1,8,2,3,7,9]
list2.sort(key=a,reverse=True)
print(list1+list2)

