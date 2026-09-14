# Question 1 – Create and Write to a File


with open("student.txt", "w") as file:
    file.write("Name: Amal\n")
    file.write("Age: 21\n")
    file.write("City: Lahore\n")

print("Student information has been written to student.txt")



# Question 2 – Read the File


# Using read()
print("\n===== Using read() =====")

with open("student.txt", "r") as file:
    content = file.read()
    print(content)


# Using readline()
print("===== Using readline() =====")

with open("student.txt", "r") as file:
    print(file.readline(), end="")
    print(file.readline(), end="")
    print(file.readline(), end="")


# Using readlines()
print("\n===== Using readlines() =====")

with open("student.txt", "r") as file:
    lines = file.readlines()

    for line in lines:
        print(line, end="")



# Question 3 – Append Data


with open("student.txt", "a") as file:
    file.write("Course: Python Programming\n")

print("\n\n===== Updated File Contents =====")

with open("student.txt", "r") as file:
    print(file.read())



# Question 4 – Handle Division Error


print("===== Division Program =====")

try:
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))

    result = num1 / num2
    print("Result:", result)

except ZeroDivisionError:
    print("Cannot divide by zero.")



# Question 5 – Handle Invalid Input


print("\n===== Age Program =====")

try:
    age = int(input("Enter your age: "))
    print("Your age is:", age)

except ValueError:
    print("Please enter a valid number.")



# Question 6 – Use else and finally


print("\n===== Square Program =====")

try:
    number = float(input("Enter a number: "))
    square = number ** 2

except ValueError:
    print("Please enter a valid number.")

else:
    print("Square:", square)

finally:
    print("Program Finished")



# Question 7 – Mini Project
# Student Result Program

print("\n===== Student Result Program =====")

student_name = input("Enter Student Name: ")

try:
    marks = float(input("Enter Obtained Marks: "))

    if marks > 100 or marks < 0:
        print("Invalid Marks")

    else:
        # Calculate Grade
        if marks >= 80:
            grade = "A"
        elif marks >= 70:
            grade = "B"
        elif marks >= 60:
            grade = "C"
        elif marks >= 50:
            grade = "D"
        else:
            grade = "F"

        print("\nStudent Name:", student_name)
        print("Marks:", marks)
        print("Grade:", grade)

except ValueError:
    print("Invalid Marks")