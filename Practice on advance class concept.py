def my_decorator(func):
    def wrapper():
        print("Something is happening before code is executed")
        func()
        print("Code executed")
    return wrapper
@my_decorator
def say_hello():
    print("Hello!")

say_hello()

def my_decorator(func):
    def wrapper(*args,**kwargs):
        print("Addition is")
        return func(*args,**kwargs)
    return wrapper
@my_decorator
def add(a,b):
    return a+b
print(add(10,50))

my_list = [1,2,3,4,5,6]
my_tuple =(1,2,3,4,5,6)
my_iter = iter(my_tuple)
print(next(my_iter))
print(next(my_iter))
print(next(my_iter))
print(next(my_iter))
print(next(my_iter))
print(next(my_iter))

def number():
    for i in range(6,13):
        yield i 
for i in number():
    print(i)

def number():
    result = []
    for i in range(13,20):
        result.append(i)
    return result
for num in number():
    print(num)

def outer(x):
    def inner(y):
        return x+y
    return inner
add = outer(5)
print(add(9))
