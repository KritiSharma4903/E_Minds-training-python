# def my_func():
#     print("Hello from a function")
# my_func()


#------------------------------*args---------------

# def my_function(*args):
#     print("Type:", type(args))
#     print("First argument:", args[0])
#     print("Second argument:", args[1])
#     print("All arguments:", args)
# my_function("Emil","Tobias","Linus")

# def my_function(*numbers):
#     total = 0
#     for num in numbers:
#         total += num
#     return total
# print(my_function(1,2,3))
# print(my_function(10,20,30,40))
# print(my_function(5))

#-------------------- **kwargs ---------------------------------

# def my_function(**myvar):
#     print("Type:", type(myvar))
#     print("Name:", myvar["name"])
#     print("Age:", myvar['age'])
#     print("All data:", myvar)

# my_function(name = "Tobias", age=30, city="Bergen")


#--------------------------- LEGB rule ---------------------------------

# x = 300
# def myfunc():
#   x = 200
# myfunc()
# print(x)


# x = "global"
# def outer():
#     x = "enclosing"
#     def inner():
#         x = "local"
#         print("Inner: ", x)
#     inner()
#     print("Outer: ", x)
# outer()
# print("Global: ", x)


#--------------------------- Decorators ---------------------------

# def my_decorator(func):
#     def wrapper():
#         print("Function Start")
#         func()
#         print("Function end")
#     return wrapper
# @my_decorator
# def say_hello():
#     print("Hello Python")
# say_hello()


#------------------------- lambda function -------------------------------

# x = lambda a : a+10                  # lambda a : a + 10 → ek function bana
# print(x(5))                     # x(5) -> a=5          (5+10 = 15)


# def myfunc(n):
#     mydoubler = myfunc(2)
#     mytripler = myfunc(3)

#     print(mydoubler(11))  
#     print(mytripler(11))


#-------------------- recursion ----------------------------
# def countdown(n):
#     if n <= 0:
#         print("Done!")
#     else:
#         print(n)
#         countdown(n-1)
# countdown(5)


# def factorial(n):
#     if n == 0 or n == 1:
#         return 1
#     else:
#         return n*factorial(n-1)
# print(factorial(5))


#---------------------------- Generators -----------------------
# def simple_gen():
#     yield "Emil"
#     yield "Tobias"
#     yield "Linus"

# gen = simple_gen()
# print(next(gen))
# print(next(gen))
# print(next(gen))

list_comp = [x*x for x in range(5)]
print(list_comp)

gen_exp = (x*x for x in range(5))
print(gen_exp)
print(list(gen_exp))
