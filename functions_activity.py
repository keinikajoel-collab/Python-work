# Part A: Basic Function
def greet_user(name):
    """Prints a personalized greeting."""
    print(f"Hello, {name}! Welcome to Python programming.")


# Part B: Function with Return Value
def calculate_area(length, width):
    """Returns the area of a rectangle."""
    return length * width


# Part C: Function with Default Parameter
def convert_temperature(temp, scale="C"):
    """Converts Celsius to Fahrenheit or vice versa.
    - If scale is 'C' (default), converts Celsius to Fahrenheit.
    - If scale is 'F', converts Fahrenheit to Celsius.
    """
    if scale.upper() == "C":
        return (temp * 9/5) + 32
    elif scale.upper() == "F":
        return (temp - 32) * 5/9
    else:
        return "Invalid scale. Use 'C' or 'F'."


# Part D: Function with Error Handling
def safe_divide(a, b):
    """Divides two numbers, returning an error message if b is zero."""
    if b == 0:
        return "Error: Division by zero"
    return a / b
