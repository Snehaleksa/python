a=set()
print(a)
print(type(a))

set1={1,2,3,"abc"}
print(set1)

a_=set([1,2,3,4,5,6])
print(a_)
print(type(a_))
for i in a_:
    print(i)


fruits=set(['apple','banana','mango']) 
fruits.add('orange'); 
print(fruits)

fruits.update(['orange','pinapple'])
print(fruits)
fruits.discard('apple')
print(fruits)
#fruits.remove('abc')
print(fruits)




days1={'monday','tuesday','wednesday','sunday'}
days2={'sunday','saturday','friday'}
print(days1|days2)
print(days1&days2)

