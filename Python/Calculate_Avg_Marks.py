# Program to calculate average marks and assign grade

# Accept marks for 5 subjects
marks = []
for i in range(1, 6):
    score = float(input(f"Enter marks for subject {i}: "))
    marks.append(score)

# Calculate average
average = sum(marks) / 5

# Assign grade based on average
if average >= 90:
    grade = "A"
elif average >= 75:
    grade = "B"
elif average >= 50:
    grade = "C"
else:
    grade = "F"

# Display result
print("\n--- Student Result ---")
print("Marks:", marks)
print("Average:", average)
print("Grade:", grade)





