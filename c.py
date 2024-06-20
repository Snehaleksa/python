#a=[1,2,3,4,5]
#b=[x**2 for x in a]
#print(b)
#list=[character for character in [1,2,3]]
#print(list)
#list=[i for i in range(11)if i%2==0]
#print(list)
#matrix
#matrix=[[j for j in range(3)]for i in range(3)]
#print(matrix)
#matrix=[]
#class Employee:
    #l1=[1,2,3]
    #l2=[2,3,4]
    #def display(self):
        #print(self.l1+self.l2)
#emp=Employee() 
#emp.display() 
#class Car:
    #def __init__(self,modelname,year):
        #self.modelname=modelname
        #self.year=year
    #def display(self):
     # print(self.modelname,self.year)
#c1=Car('toyota',2016)
#c1.display()            
#class Employee:
    #def __init__(self,name,id):
        #self.id=id
        #self.name=name
    #def display(self):
        #print(self.id,self.name)
#emp1=Employee('john',101)
#emp2=Employee('david',102)
#emp1.display()
#emp2.display() 
#class Student:
    #def __init__(self,name):
        #print('this is parametrized constructor')
        #self.name=name
        #def show(self):
            #print('hello',self.name)
#student= Student("john")
#student.show() 

class Student:
    def __init__(self,name,id,age):
        self.name=name
        self.id=id
        self.age=age
s=Student('john',101,23) 
 
#print(getattr(s,'name')) 
                          


    


