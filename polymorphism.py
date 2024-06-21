class Numbers:
    def cat(self):
        print('i can eat')
class Cat(Numbers):
    def cat(self):
        print('I sound like meow')
d=Cat()
d.cat() 
class A:
    def a(self):
        print('1 is working')
class B(A):
    def a(self):
        print('2 is working')
class C(A):
    def a(self):
        print('3 is working')
obj1=A()
obj2=B()  
obj3=C()
obj1.a()
obj2.a()
obj3.a()                    



