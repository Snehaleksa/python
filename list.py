list=[1,2,'a',3,'b']
print(list)
print(list[1])
print(list[0])
print(list[-1])

a=['h','e','l','l','o','w','o','r','l','d']
print(a[2:])
print(a[5:])
print(a[2:5])
print(a[:])

b=[1,2,3,4,5]
b.append(32)
print(b)
b.insert(3, 12)
print(b)


c=[2,3,4]
d=['a','b','c']
d.extend(c)
print(d)

fruits=['apple','banana','mango']
fruits[2]='orange'
print(fruits)

numbers=[1,2,3,4,5,6,7,8]
del numbers[2]
del numbers[-1]
print(numbers)

languages=['python','java','c++','c','Rust']
del languages[0:2]
print(languages)

lang=['python','java','c++','c','Rust']
lang.remove('java')
print(lang)

f=[1,2,3,4,5]
f.reverse()
print('reversed list',f)

g=[1,2,3,4]
g.clear()
print(g)

h=[2,4,8,10]
removed_element=h.pop(2)
print(removed_element)

list1=[1,2,3,4]
l=list1*3
print(l)

list2=[1,2,3,4,5]
list3=[6,7,8,9]
l=list2+list3
print(l)

list4=[1,2,3,4,5,6,7,8,9]
for i in list4:
    print(i)



list5=[1,2,3,4,5,6,7,8,9,10]
for i in list5:
    if i%2==0:
        print(i)

list6=[1,2,3,4,5,6]  
for i in list6:
    if i%2==1:
        print(i)     

z=['abc','def','ghi','jkl']
print('xyz' in z) 
print('def'in z)  

_list1=(103,675,321,782,200)
print(max(_list1))
print(min(_list1))

_list2=['a','b','c','d']
_list3=['b','d','c','f','g']
intersection1=set(_list2).intersection(_list3)
print(intersection1)
xyz=set(_list2)&set(_list3)
print(xyz)