# %%
# 5 Important Decorators that you need to Know
    # 1. property
    # 2. staticmethod (to call a method that is not binded to Instance)
    # 3. classmethod (to call a method that is binded to Class but not Instance, so that you can access Class Attributes or Methods. Class is   passed as a argument instead of Self)
    # 4. functools.cache
    # 5. dataclass

# Decorators Examples
# Using existing method as a Decorated function
import time
def tictoc(func):
    def wrapper():
        tl = time.time()
        func()
        t2 = time.time()-tl
        print(f'{func.__name__} ran in'\
              f' {t2} seconds')
    return wrapper

@tictoc
def do_this():
    # Simulating running code..
    time.sleep (3)

@tictoc
def do_that():
    # Simulating running code..
    time.sleep (2)
    
do_this()
do_that()
print('Done')
# %%
def myadd(func):
    def wrapper(*x):
        print(f'I am Sandeep')
        print(func(*x))
    return wrapper

@myadd
def yadd(a,b):
    return a+b

f = yadd
f(2,3)
# %%
# Encapsulation in Python is achieved using classes and objects. Here are some ways to incorporate encapsulation in Python using Private Variables (Name Mangling), Properties (Decorators), Public Methods (Decorators)

# Name Mangling
# Python does not support strict private and protected variables. Private variables in Python are typically denoted by using a double underscore prefix (__) before the variable name. This prefix triggers the name mangling process, which replaces the variable name with a mangled version that includes the class name (_MyClass__private_value). This mangled name is used internally within the class, making it less accessible from outside the class.

class MyClass:
    def __init__(self, private_value):
        self.__private_value = private_value

    def get_private_value(self):
        return self.__private_value

obj = MyClass(10)
print(obj.get_private_value())  # Output: 10
print(obj.__private_value)  # Output: AttributeError
print(obj._MyClass__private_value)  # Output: 10
# %%
