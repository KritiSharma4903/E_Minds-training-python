lst = [10,45,23,89,51]

largest = second_largest = -1

for num in lst:
    if num > largest:
        second_largest = largest
        largest = num
    elif num > second_largest and num != largest:
        second_largest = num

print("Second largest number is: ", second_largest)












