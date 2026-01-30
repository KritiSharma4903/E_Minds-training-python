#------------- Reverse a String --------------------

# num = int(input("Enter a number: "))
# rev = 0
# while num > 0:
#     digit = num%10
#     rev = rev * 10 + digit
#     num //= 10
# print("Reversed number is: ", rev)


#---------------Palindrome number ------------------------

# num = int(input("Enter a number: "))
# temp = num
# rev = 0
# while num > 0:
#     digit = num%10
#     rev = rev*10+digit
#     num //= 10
# if rev == temp:
#     print("Palindrome number")
# else:
#     print("Not Palindrome number")


#-------------- Factorial--------------------------

# n = int(input("Enter number of terms: "))
# fact = 1
# for i in range(1, n+1):
#     fact *= i
# print("Factorial = ", fact)


#-------------count digit in a numbers------------------

# num = int(input("Enter a number: "))
# count = 0
# if num == 0:
#     count = 1
# else:
#     while num > 0:
#         count += 1
#         num //= 10
# print("Numbers of digit: ", count)


#---------------- Even or Odd -----------------------
# n = int(input("Enter a number: "))
# if n%2==0:
#     print("Even number")
# else:
#     print("Odd number")


#---------------------------- Reverse an array ---------------------------------
# arr = [1,2,3,4,5]
# start = 0
# end = len(arr - 1)
# while start < end:
#     arr[start], arr[end] = arr[end], arr[start]

#     start += 1
#     end -= 1
# print("Reserved array: ", arr)


#--------------------- Find Maximum and Minimum of Array ----------------------------------

# arr = [4,7,1,9,2,5]
# max_num = arr[0]
# min_num = arr[0]
# for num in arr:
#     if num > max_num:
#         max_num = num
#     if num < min_num:
#         min_num = num
# print("Maximum element: ",max_num)
# print("Minimum element: ", min_num)


#--------------------------- Move all zeroes to the end -----------------------------

# arr = [0,1,0,3,12]
# result = []
# zero_count = 0
# for num in arr:
#     if num != 0:
#         result.append(num)
#     else:
#         zero_count += 1
# for i in range(zero_count):
#     result.append(0)
# print(result)


#--------------------- Rotate an array by K steps -------------------------

#------ Right Rotation---------
# arr = [1,2,3,4,5]
# k = 2
# n = len(arr)
# for i in range(k):
#     last = arr.pop()
#     arr.insert(0, last)
# print(arr)

#------- Left Rotation ----------
# arr = [1,2,3,4,5]
# k = 2
# for i in range(k):
#     first = arr.pop(0)
#     arr.append(first)
# print(arr)


# ------------Check if a string is a palindrome-----------------

# s = input("Enter a string: ")
# rev = ""
# for ch in s:
#     rev = ch + rev
# if s == rev:
#     print("Palindrome")
# else:
#     print("Not Palindrome")


#--------------------- Check if two strings are anagrams -----------------------------

# s1 = input("Enter first string: ")
# s2 = input("Enter second string: ")

# if len(s1) != len(s2):
#     print("Not Anagram")
# else:
#     freq1 = {}
#     freq2 = {}

# for ch in s1:
#     freq1[ch] = freq1.get(ch,0)+1
# for ch in s2:
#     freq2[ch] = freq2.get(ch,0)+1

# if freq1 == freq2:
#     print("Anagram")
# else:
#     print("Not Anagram")


#------------------------ BINARY SEARCH----------------------

def binary_search(arr,target):
    low = 0
    high = len(arr)-1

    while low <= high:
        mid = (low + high)//2

        if arr[mid] == target:
            return mid
        elif target < arr[mid]:
            high = mid-1
        else:
            low = mid+1
    return -1

arr = [2,4,6,8,10,12,14]
target = 10

result = binary_search(arr, target)

if result != -1:
    print("Element found at index:", result)
else:
    print("Element not found")



#------------------------ LINEAR SEARCH -------------------------

def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1 

arr = [4,7,1,9,3]
target = 9

result = linear_search(arr, target)

if result != -1:
    print("Element found at index: ", result)
else:
    print("Element not found")

    