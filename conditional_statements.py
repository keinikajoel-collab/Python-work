"""
these apply is scenarios where we need to make a number/ a decision.

# syntax
## If
if condition:
    logic
"""

### Examples: Adult age check.

age = int(input("Enter your age:"))

if age >=18:
    print("Your are an adult")

## Example 2: Basic Calc
print("MENU")
print("1. + \n 2. - \n 3. x \n 4. /")
#operator = int(input("Please make your choice"))

"""
IF ELSE

## Syntax
if condition:
    logic
else:
    logic
"""
age = int(input("Enter your age"))

if age >= 18:
    print("Your are an adult")

else:
    print("Your are a child.")

"""
IF, ELSE IF< ELSE

## Syntax

if condition:
    logic
elif condition:
    logic
else:
    logic
"""

print("Select your age: \n1. 18 and above. \n 2. 17 and below \n")
age=int(input("Enter your age:"))

if age == 1:
    print("Your are an adult")
elif age==2:
    print("Your are a child.")
else:
    print("Provide a valid age range")

## Example 2: Basic Calc
print("MENU")
print("1. + \n2. - \n3. x \n4. /")
operator_selection = int(input("Please make your choice: "))
first_number = float(input("Enter the first number: "))
second_number = float(input("Enter the second number: "))

if operator_selection == 1:
    summation = first_number + second_number
    print(f"The sum is {summation}")

elif operator_selection == 2:
    difference = first_number-second_number
    print(f"The difference is{difference}")

elif operator_selection == 3:
    product = first_number*second_number
    print(f"The prpduct is{product}")

elif operator_selection == 4:
    product = first_number/second_number
    print(f"The quotient is{quotient}")

else:
    print("Choose a right operator")