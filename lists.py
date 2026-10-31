"""
A list is an ordered mutable collection of items in any type.
- it is represented by[] in python

"""

## 1.Examples

list = [1, True, 3.56, "Samuel" , [34, 5]]## mixed data types
fruits = ["Apples", "oranges", "Mangoes"] ## a single data type
students = []## empty

##n2. Accessing items in a list
## index
print(fruits[0])

print(fruits[-1])
print(list[-3:-4])

##3. List operations
print(f"Current collection:{fruits}")
##3.1 Adding an items to list
fruits.append("pineapples")
print(f"New collection:{fruits}")

##3.2 Inserting items into a list
fruits.insert(2,"Bananas")
print(f"New collection:{fruits}")
fruits.insert(3,"watermelon")
print(f"New collection:{fruits}")
 
##3.3 Adding a number of items to a list
fruits.extend(["grapes", "kiwi", "dragon fruit"])
print(f"New collection: {fruits}")

##3.4 Deleting an item
fruits.pop()  ## remove the last items from the list
print(f"New collection:{fruits}")


##3.5 Removing a specific item
fruits.remove("grapes")
print(f"New collection:{fruits}")


##3.6 Removing items using their index
fruits.pop(3)
print(f"New collection:{fruits}")

## 4. Other operations
###4.1 len function (the number of items in a list)
print("The number of items in the list collection is", len(fruits))
print("The number of items in the fruit collection is", len(fruits))

## 4.2.1Sort operation(sort)
marks =[89, 45, 88, 94, 54, 23, 100]
marks.sort()
print(marks)

## 4.2.2 Sort operation (sorted)
marks = [89, 45, 88, 94, 54, 23, 100]
sorted_marks = sorted(marks)
print(sorted_marks)

## 4.3 Reverse operation 
sorted_marks.reverse()
print(sorted_marks)

marks = [89, 45, 88, 94, 54, 23, 100]
marks.sort()
print(f"Ascending order is :{marks}")
print(f"Descending order is :{marks[::-1]}")

##5. List comprehensions
## This is aconcise way to build lists from existing iterables

##example: list of squares
squares = [x**2 for x in range(10)]
print(squares)

even_numbers = [even for even in range(100)if even%2 ==0]
print(even_numbers)

total_even = sum(even_numbers)
print(total_even)

odd_numbers = [odd for odd in range(100)if odd%2 ==1]
print(odd_numbers)
