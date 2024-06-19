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
class Car:
    def __init__(self,modelname,year):
        self.modelname=modelname
        self.year=year
    def display(self):
        print(self.modelname,self.year)
c1=Car('toyota',2016)
c1.display()            



    


