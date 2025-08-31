# Get input from the user
score = int(input("Enter your test score: "))

# Use conditional statements to determine the grade
if score >= 90:
    print("Grade: A")
elif score >= 80:
    print("Grade: B")
elif score >= 70:
    print("Grade: C")
elif score >= 60:
    print("Grade: D")
else:
    print("Grade: F")

print("End of grading program.")