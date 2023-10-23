## Functions can have inputs/functionality/output
def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2

##Functions are first-class objects, can be passed around as arguments e.g. int/string/float etc.

def calculate(calc_function, n1, n2):
    return calc_function(n1, n2)

result = calculate(add, 2, 3)
print(result)

##Functions can be nested in other functions

def outer_function():
    print("I'm outer")

    def nested_function():
        print("I'm inner")

    nested_function()

outer_function()

## Functions can be returned from other functions
def outer_function():
    print("I'm outer")

    def nested_function():
        print("I'm inner")

    # 返回，不是现在激活()
    return nested_function

inner_function = outer_function()
inner_function


## Simple Python Decorator Functions
import time

def delay_decorator(function):
    def wrapper_function():
        time.sleep(2)
        #Do something before
        function()
        function()
        #Do something after
    return wrapper_function

# 装饰器：设置在函数运行前/后运行的东西、或更改函数
@delay_decorator
def say_hello():
    print("Hello")

#With the @ syntactic sugar
@delay_decorator
def say_bye():
    print("Bye")

#Without the @ syntactic sugar
def say_greeting():
    print("How are you?")

# 装饰器是语法糖，简化了下面的语法
decorated_function = delay_decorator(say_greeting)
decorated_function()

import time
current_time = time.time()
print(current_time) # seconds since Jan 1st, 1970

# Write your code below 👇

def speed_calc_decorator(function):
  def wrapper_calculation():
    start_time = time.time()
    function()
    end_time = time.time()
    print(f"function.__name__ run speed: {end_time - start_time}s")
  return wrapper_calculation

@speed_calc_decorator
def fast_function():
  for i in range(1000000):
    i * i

@speed_calc_decorator
def slow_function():
  for i in range(10000000):
    i * i

fast_function()
slow_function()

