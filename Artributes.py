class Student:
    def __init__(self,name,id,age):
        self.name=name
        self.id=id
        self.age=age
s=Student('john',101,22) 
print(getattr(s,'name','id')) 
setattr(s,'age',23)
print(getattr(s,'age'))     
print(hasattr(s,'ab'))
delattr(s,'age')
print(s.age)

