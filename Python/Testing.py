# import math

# Mylst =[2,4,8,10]

# for i in Mylst:
#     x = i**2
#     print(x)



class Calculator():

    def sum(self,a,b):
        return a+b

    def sub(self,a,b):
        return a-b
    
    def mul(self,a,b):
        return a*b

calc = Calculator()
print(calc.sum(4,5))
print(calc.sub(9,3))
print(calc.mul(3,2))