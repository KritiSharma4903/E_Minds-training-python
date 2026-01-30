# ------------------------------ Range---------------------------------------
# print(list(range(5)))
# print(list(range(1, 6)))
# print(list(range(5, 20, 3)))

# -----------------------------Iterators-------------------------------------

# mystr = ("apple", "banana", "cherry")
# myit = iter(mystr)
# print(next(myit))
# print(next(myit))
# print(next(myit))
# print(next(myit))
# print(next(myit))
# print(next(myit))


# class MyNumbers:
#     def __iter__(self):
#         self.a = 1
#         return self
    
#     def __next__(self):
#         x = self.a
#         self.a += 1
#         return x

# myclass = MyNumbers()
# myiter = iter(myclass)

# print(next(myiter))
# print(next(myiter))
# print(next(myiter))
# print(next(myiter))
# print(next(myiter))


#-------------------------- Module --------------------------------

# import Module as mx

# mx.greeting("Kriti")


#----------------------- Date-Time ------------------------
import datetime
x = datetime.datetime.now()
print(x.year)
print(x.strftime("%A"))


