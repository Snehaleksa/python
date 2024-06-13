def name():
    return 'hello'
print(name())


def a(num):
    return num**2
b=a(6)
print(a(6))

def c(string):
    return len(string)
print (c('Python'))
print (c('Function'))


def d(n1,n2=20):
    print('n1 is ',n1)
    print('n2 is ',n2)
d(10)

def e(n3,n4):
    print('number1 is ',n3)
    print('number2 is ',n4)
print('without using keyword')
e(n3=50,n4=20)  