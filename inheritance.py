#single inheritance
#class Animal:
    #def speak(self):
        #print('Animal speaking')
#class Dog(Animal):
    #def bark(self):
        #print('dog barking')
#d=Dog()
#d.bark()
#d.speak() 
#Multi inheritance
#class Animal:
    #def speak(self):
        #print('Animal Speaking')
#class Dog(Animal):
    #def bark(self):
        #print('Dog barking')
#class DogChild(Dog):
    #def eat(self):
        #print('Eating')
#d=DogChild()
#d.bark()
#d.speak()
#d.eat()                                       
#multiple inheritance
class Calculation1:
    def Sum(self,a,b):
        return a+b
class Calculation2:
    def mul(self,a,b):
        return a*b
class Derived(Calculation1,Calculation2):
    def divide(self,a,b):
        return a/b
d=Derived()
print(d.Sum(10,20))
print(d.mul(10,20))
print(d.divide(10,20))    
#Hyrarchical
class Parent:
    def func1(self):
        print('this function is in parent class')
class Child1(Parent):
    def func2(self):
        print('This function is in child2')
class Child2(Parent):
    def func3(self):
        print('this function is in child 2')
object1=Child1()
object2=Child2()
object1.func1()
object1.func2()
object2.func1()
object2.func3()


class Animal:
    def speak(self):
        print('speaking')
class Dog(Animal):
    def speak(self):
        print('barking')
d=Dog()
d.speak()  

class Bank:
    def getroi(self):
        return 10
class SBI(Bank):
    def getroi(self):
        return 7
class ICICI(Bank):
    def getroi(self):
        return 8
b1=Bank()
b2=SBI()
b3=ICICI()
print('Bank Rate of interest',b1.getroi())
print('SBI Rate of interest',b2.getroi())
print('ICICI Rate of interest',b3.getroi()) 

class Bird:
    def intro(self):
        print('There are many types of birds')
    def flight(self):
        print('Most of the birds can fly but some cannot')
class Sparrow(Bird):
    def flight(self):
        print('Sparrow can fly')
class Ostrich(Bird):
    def flight(self):
        print('Ostrich cannot fly')
obj1=Bird() 
obj2=Sparrow()
obj3=Ostrich()  
obj1.intro()
obj1.flight()
obj2.intro()
obj2.flight()
obj3.intro()
obj3.flight()                     
            
#class Animal:
    #def cat(self):
        #print('i can eat')
#class Cat(Animal):
    #def cat(self):
        #print('I sound like meow')
#d=Cat()
#d.cat()
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