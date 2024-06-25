def my_decorator(func):
    def wrapper():
      print('someting happen before')
      func()
      print('something happen after')
    return wrapper

@my_decorator
def say_hello():
   print('Hello') 
say_hello()    

