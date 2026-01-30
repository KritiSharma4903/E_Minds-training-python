lst = list(map(int,input("Enter the numbers of list: ").split()))
print(lst)

greatest = lst[0]

for i in lst:
    if i > greatest:
        greatest = i 

print("Greatest number is: ", greatest)



