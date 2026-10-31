


# swap 
drink_a = "water"
drink_b = "juice"

print(" drink_a =", drink_a)
print(" drink_b =", drink_b)

# swap them
drink_a, drink_b = drink_b, drink_a

#result after swapping 
print(" drink_a =", drink_a)
print(" drink_b =", drink_b)

#swap them back 
drink_a, drink_b = drink_b, drink_a
print(" drink_a =", drink_a)
print(" drink_b =", drink_b)




word = "University"
print("The word has", len(word), "letters")

result1 = 7 // 2
print("\n7 divided by 2 =", result1)


age_as_text   = "20"           # this is a string — you can't add to it
age_as_number = int(age_as_text)  # now it's a real integer

print("Type before:", type(age_as_text))    # str
print("Type after: ", type(age_as_number))  # int
print("In 5 years you'll be:", age_as_number + 5)


height = 5.9
print("\nHeight as float:", height)
print("Height as int:  ", int(height))


score = 85
message = "Your score is: " + str(score) + " out of 100"
print(message)


PI              = 3.14159
MAX_STUDENTS    = 40
SCHOOL_NAME     = "Uganda Christian University"
PASSING_GRADE   = 50

radius = 7
area_of_circle = PI * radius * radius

print("School:", SCHOOL_NAME)
print("Max class size:", MAX_STUDENTS)
print("Passing grade:", PASSING_GRADE, "%")
print("Area of circle with radius", radius, "=", area_of_circle)

a = 10
b = 3

print("a =", a, "  b =", b)
print()
print("a + b  =", a + b)     # Addition       → 13
print("a - b  =", a - b)     # Subtraction    → 7
print("a * b  =", a * b)     # Multiplication → 30
print("a / b  =", a / b)     # Division       → 3.333...
print("a // b =", a // b)    # Floor Division → 3  (no decimal)
print("a % b  =", a % b)     # Modulo         → 1  (remainder)
print("a ** b =", a ** b)    # Exponent       → 1000 (10³)


score = 100
print("Starting score:", score)

score += 10    # same as: score = score + 10
print("After bonus (+10):", score)

score -= 5     # same as: score = score - 5
print("After penalty (-5):", score)

score *= 2     # same as: score = score * 2
print("After doubling (*2):", score)

score //= 3    # same as: score = score // 3
print("After dividing by 3 (//3):", score)



is_student = True
has_id_card = False

print("is_student  :", is_student)
print("has_id_card :", has_id_card)
print()

# Can they enter the library?
can_enter = is_student and has_id_card
print("Can enter library? (student AND has ID):", can_enter)   # False

# Can they get a discount?
can_discount = is_student or has_id_card
print("Can get discount? (student OR has ID):", can_discount)  # True

# Are they NOT a student?
print("Is NOT a student:", not is_student)   # False

# Real-world example: access to exam hall
has_paid_fees   = True
registered      = True
has_been_barred = False

can_sit_exam = has_paid_fees and registered and (not has_been_barred)
print("\nCan sit exam?", can_sit_exam)   # True



