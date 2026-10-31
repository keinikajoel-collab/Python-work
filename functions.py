"""
a function is a reusable price of code with a specific purpose.

CAtegories of functions:
1. Built in functions
2. User defined fuctions
3. Reclusive functions
4. Lambda functions
5. Async functions
6. Higher oreder functions
"""

## 1.  Built in functions
"""
These are functions that come with python after installtion.
Examples: print(), sum(), len(), tyeof(), float(),
"""

students_marks = [98, 57, 98, 90]
print(f"length of the list:{len(students_marks)}")

"""
Types of functions
1. Void functions
2. Returning functions
"""

## 2. User defined functions
"""
These are custom made by theprogrammer to be uniquely utilized in the program.

We use the 'def' key word to make these functions.

They can have parameters or can be made without parameters.

"""

# Example 1
def greetings(name, course):
    print(f"Hi, {name}! 👋 \n Welcome to {course}")

greetings("Joel", "Structured Programming")

## Returning functions:
"""
These use the return key word at the end to output results
"""

def addition(number1, number2, number3):
    summation = number1 + number2 + number3
    return summation

print(addition(2,78,50))

def subtraction(number1, number2, number3):
    difference = number1 - number2 - number3
    return difference

def multiplication(number1, number2, number3):
    product = number1 * number2 * number3
    return product

def division(number1, number2, number3):
    quotient = number1/number2/number3
    return quotient

def menu():
    while True:
        print("Simple calc")
        print("Choose operation")
        print("1. Addition\n")
        print("2. Subtraction\n")
        print("3. Multiplication\n")
        print("4. Division\n")
        print("5. Exist")

        chioce = int(input("Choose an operation"))
        if choice == 5:
            print("Goodbye...")
            break 

        number_1 = float(input("Enter first number: "))
        number_2 = float(input("Enter second number: "))
        number_3 = float(input("Enter third number"))

        if choice == 1:
            print(addition(number1, number2, number3))
        elif choice == 2:
            print(subtraction(number1, number2, number3))
        elif choice == 3:
            print(multiplication(number1, number2, number3))
        elif choice == 4:
            print(division(number1, number2, number3))
        else:
            print("Choose a number between 1-4")
    menu()

