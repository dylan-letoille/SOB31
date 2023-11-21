# Calculating Grades (ok, let me think about this one)

"""Write a program that will average 3 numeric exam grades, return an average test score, a corresponding letter
grade, and a message stating whether the student is passing. (made comment multy line for readability) """

# Average	Grade
# 90+	A
# 80-89	B
# 70-79	C
# 60-69	D
# 0-59	F

# Exams: 89, 90, 90
# Average: 90
# Grade: A
# Student is passing.

# Exams: 50, 51, 0
# Average: 33
# Grade: F
# Student iis failing.

exam_one = int(input("Input exam grade one: "))

exam_two = int(input("Input exam grade two: "))  # removed extra bracket and changed input value to int

exam_three = int(input("Input exam grade three: "))  # changed str to int and changed 3 to three

grades = [exam_one, exam_two, exam_three]  # separated variables with commas and fixed the last variable
sum1 = 0  # changed sum to sum1 so built-in function is not shadowed
for grade in grades:  # changed grade to grades to match the list
    sum1 = sum1 + grade  # re indented lines to be multiple of 4

avg = sum1 / len(grades)  # changed grdes to grades
avg = round(avg)  # rounded average to a whole number
if avg >= 90:
    letter_grade = "A"
elif 80 <= avg < 90:  # added colon and simplified condition
    letter_grade = "B"
elif 69 < avg < 80:  # simplified condition
    letter_grade = "C"  # changed single quote to double quote
elif 69 >= avg >= 65:  # simplified condition
    letter_grade = "D"
else:  # changed elif to else
    letter_grade = "F"

print("Exams: ", end="")  # changed Exam to Exams and modified the for loop so output is in line with examples above
for grade in grades:
    print(str(grade), end=" ")

print("\nAverage: " + str(avg))

print("Grade: " + letter_grade)

if letter_grade == "F":  # changed letter-grade to letter_grade and replaced is with ==
    print("Student is failing.")  # added parenthesis around printed sentence
else:
    print("Student is passing.")  # added parenthesis around printed sentence
