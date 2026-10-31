"""
 1. Parameter - this is the variable definition in a function
 2. Argument -> the actual value placed in the function.

 """

## Example 1:
def addition(number1, number2, number3): ### parameters number1, number2, number3
    summation = number1+number2+number3
    return summation

addition(23,45,56) ## the arguments are 23, 45, 56
addition(number3=56, number1=23, number2=99)
"""
number1 -> 23
number2 -> 45
number3 -> 56
"""


def grade_book(name, course, marks, **kwargs):
   return [marks, course, name]

grade_book(course="bsit", name="John", marks=98)

## *args
## we allow extra arguments into the function

def summation(*args):
   print(args)
   return sum(args)

print(summation(23,45,56))

## **kwargs
## enables us to add extra parameters

def student_info(**kwargs):
   print(f"Student details : {kwargs}")
   return kwargs

student = student_info(student_name = "Charles", course = "Bsit", access_number = "B36771", reg_number="M26B13/022")


"""
Python Dictionary
This is a data structure that works with key-value pairs
"""
print(student)## contains student information from the function

##1. reading values from a dictionary
print(f"Student name: {student["student_name"]}")

print(f"course: {student["course"]}")
print(f"access_number: {student["access_number"]}")
print(f"reg_number: {student["reg_number"]}")