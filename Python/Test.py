#------------------------------- First 10 prime no.------------------------------------

# n = 10
# count = 0
# num = 2

# while count < n:
#     for i in range(2, num):
#         if num%i == 0:
#             break
#     else:
#         print(num, end=" ")
#         count += 1
#     num += 1

#------------ Reverse a string without reverse() --------------------------------------

# string = "Python"
# rev = ""
# for ch in string:
#     rev = ch+rev
# print(rev)


#------------------ Find factorial of a number --------------------------
# n = 5
# fact = 1
# for i in range(1, n+1):
#     fact *= i
# print(fact)


#----------------- Check Palindrome number -------------
# n = 1223221
# temp = n
# rev = 0

# while n>0:
#     rev = rev*10 + n%10
#     n //= 10
# if temp == rev:
#     print("Palindrome")
# else:
#     print("Not Palindrome")


# ------------------- Count Vowel in a string----------------------

# s = "education"
# count = 0
# for ch in s:
#     if ch in "qeiouAEIOU":
#         count += 1
# print(count)

# -----------------CLASS & OBJECT--------------------

# class Student:
#     def __init__(self,name, marks):
#         self.name = name
#         self.marks = marks 

#     def display(self):
#         print(self.name, self.marks)
# s1 = Student("Kriti", 90)
# s1.display()


# class Rectange:
#     def __init__(self, l, b):
#         self.l = l 
#         self.b = b 

#     def area(self):
#         print("Area: ", self.l*self.b)

# r = Rectange(10, 5)
# r.area()


# class Demo:
#     def show(self):
#         print("Hello Python")
# d = Demo()
# d.show()


# class A:
#     def showA(self):
#         print("Class A")

# class B(A):
#     def showB(self):
#         print("Class B")
# obj = B()
# obj.showA()
# obj.showB()


# class Test:
#     count = 0
#     def __init__(self):
#         Test.count += 1
# t1 = Test()
# t2 = Test()
# t3 = Test()
# print("Objects:", Test.count)




# s = "python"
# print(s[::-1])



# s = "madam"
# print("Palindrome" if s == s[::-1] else "Not")


# n = 5                                                                 # Factorial
# fact = 1
# for i in range(1, n+1):
#     fact *= i
# print(fact)


# a,b = 0,1                                                                       # Fibonacci
# for i in range(5):
#     print(a, end=" ")
#     a,b = b, a+b


# n = 7
# print("Even" if n%2 == 0 else "Odd")


# lst = [10, 5, 30]
# print(max(lst))


# s = "education"
# print(sum(1 for ch in s if ch in "aeiouAEIOU"))


# n = 123
# print(sum(map(int, str(n))))


# a,b = 5, 10
# a,b = b,a
# print(a,b)



# n = 7
# for i in range(2, n):
#     if n%i == 0:
#         print("Not Prime")
#         break
# else:
#     print("Prime")



# lst = [1,2,2,3]
# print(list(set(lst)))


# #------------------ count character frequency------------
# s = "interview"
# freq = {}
# for ch in s:
#     freq[ch] = freq.get(ch, 0) + 1
# print(freq)


# s = "aabbcde"
# for ch in s:
#     if s.count(ch) == 1:
#         print(ch)
#         break


# arr = [1,2,3,5]
# n = 5
# print(n*(n+1)//2 - sum(arr))


# n = 153
# temp = n
# s = 0
# while n > 0:
#     d = n % 10
#     s += d**3
#     n //= 10
# print("Armstrong" if s == temp else "Not")



# lst = [10, 20, 30]
# lst.sort()
# print(lst[-2])


# a = "listen"
# b = "silent"
# print(sorted(a) == sorted(b))


# s = "python is easy"
# print(len(s.split()))


# lst = [10,20,30]
# x = 20
# print("Found" if x in lst else "Not Found")


# class A:
#     def show(self):
#         print("Class A")
# class B(A):
#     pass
# obj = B()
# obj.show()


# a = [1,2,3,4]
# b = [3,4,5,6]
# common = []
# for i in a:
#     if i in b:
#         common.append(i)
# print(common)


# lst = [10,2,48,98,5]
# small = lst[0]
# large = lst[0]

# for i in lst:
#     if i < small:
#         small = i
#     if i > large:
#         large = i
# print("Smallest: ", small)
# print("Largest: ", large)



quantity = 3
itemno = 567
price = 49
myorder = "I want {} pieces of item number {} for {:.2f}"
print(myorder.format(quantity, itemno, price))















































