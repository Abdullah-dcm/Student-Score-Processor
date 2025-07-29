# 📝 Student Scores Processor - Session 4: Conditionals and Control Flow
# Welcome to Python School! Let's help you process your exam scores like a pro 📚
# This session will teach you how to use math and logic in Python.

# Print welcome message

print(" Welcome to Score Processing System \n")
print("We'll calculate your percentage and check if you passed!\n")

# Ask for student name

std_name = input("Enter your name?: ")

# Take marks for three subjects (out of 100 each)

print("\nEnter your marks out of 100 for the following subjects:")

maths = float(input("Mathematics : "))
science = float(input("Science : "))
english = float(input("English : "))

# Total marks possible

total_marks = 300

# Total obtained

marks_obtained = maths + science + english

# Calculate average and percentage

average = marks_obtained /  3
percentage = (marks_obtained / total_marks) * 100  

# Round for nicer output

avg_rounded = round(average, 2)
percentage_rounded = round(percentage, 2)

# Print student report

passing_marks = 40.0
has_passed = percentage >= passing_marks
print("\n\n Generating your Report...\n")
print("~" * 40)

# Display results

print("Student:", std_name, end=" \n")
print("Marks:", "Math =", maths, ", Science =", science, ", English =", english, end=" \n")
print("\nTotal Marks:", marks_obtained, "/ 300", end=" \n")
print("\nAverage Score:", avg_rounded, end=" \n")
print("\nPercentage:", percentage_rounded, "%", end=" \n")


# 🎊 The fun part: Decide pass or fail based on a threshold (e.g., 40%)
# Print a message based on pass or fail (hint: use if-else!)

print("\n\n Passed: ", has_passed)

# Encouraging message
print("~" * 40)
print("\nKeep working hard! You can do much better.\n")

# 💡 Notes for learners:
# - Arithmetic: + for addition, / for division, () controls order (precedence).
# - Comparison: >= checks "greater than or equal to".
# - A comparison returns True or False, which we can print as a result.