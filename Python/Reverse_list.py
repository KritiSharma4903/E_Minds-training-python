class ReverseList:
    def reverse_list(self, mylist):
        reversed_list = []
        for i in range(len(mylist) - 1, -1, -1):
            reversed_list.append(mylist[i])
        return reversed_list

obj = ReverseList()

lst = [1, 2, 3, 4, 5]

result = obj.reverse_list(lst)

print("Reversed List:", result)

















# class ReverseList:
#     def reverse_list(self, mylist):
#         return mylist[::-1]

# # object creation
# obj = ReverseList()

# # function call through object
# numbers = [1, 2, 3, 4, 5]
# result = obj.reverse_list(numbers)

# print(result)
