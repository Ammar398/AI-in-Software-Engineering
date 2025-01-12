#Exercise Python input /output Basic operations
#(i) Swap the Values of Four Variables

# Input four values
a = 2
b = 56
c = 78
d = 9

print("Before swapping:")
print(f"a = {a}, b = {b}, c = {c}, d = {d}")

# Swap the values in a cyclic order
a, b, c, d = d, c, b, a

print("After swapping:")
print(f"a = {a}, b = {b}, c = {c}, d = {d}")

#(ii) Convert Temperatures Between Celsius and Fahrenheit

# Convert temperatures
def celsius_to_fahrenheit(celsius):
    # Convert Celsius to Fahrenheit
    fahrenheit = (celsius * 9/5) + 32
    return fahrenheit

# Input temperature in Celsius
celsius = float(input("Enter temp in Celsius: "))

# Calculate Fahrenheit
fahrenheit = celsius_to_fahrenheit(celsius)

print(f"Temperature in Fahrenheit is: {fahrenheit:.2f}")

#Exercise: Lists

#(i) Playing with List Functions

# Define a sample list
lst = ['a', 'b', 'c', 'a', 'd']

# Reverse the list
lst.reverse()
print("Reversed list:", lst)  # Output: ['d', 'a', 'c', 'b', 'a']

# Count occurrences of an element
count_a = lst.count('a')
print("Count of 'a':", count_a)  # Output: 2

# Append a new element to the list
lst.append('z')
print("List after appending 'z':", lst)  # Output: ['d', 'a', 'c', 'b', 'a', 'z']

# Extend the list with another list
lst.extend(['x', 'y'])
print("List after extending:", lst)  # Output: ['d', 'a', 'c', 'b', 'a', 'z', 'x', 'y']

# Remove a specific element
lst.remove('c')
print("List after removing 'c':", lst)  # Output: ['d', 'a', 'b', 'a', 'z', 'x', 'y']

# Sort the list
lst.sort()
print("Sorted list:", lst)  # Output: ['a', 'a', 'b', 'd', 'x', 'y', 'z']

#(ii) Count Strings with Matching First and Last Characters

def count_strings(lst):
    count = 0
    for string in lst:
        if len(string) >= 2 and string[0] == string[-1]:  # Check length and first-last character
            count += 1
    return count

# Sample List
sample_list = ['abc', 'xyz', 'aba', '1221']

# Call the function
result = count_strings(sample_list)

print("Expected Result:", result)  # Output: 2

#Exercise: Dictionaries 

#(i) Using dir and help to Explore Dictionary Functions

# Define a sample dictionary
sample_dict = {'a': 1, 'b': 2, 'c': 3}

# Using dir() to view available methods
print(dir(dict))  # Lists all available dictionary methods

# Example: Using help() on the `keys` method
help(dict.keys)  # Shows information about the `keys` method

# Example implementations of some methods:
print("Original Dictionary:", sample_dict)

# Getting dictionary keys
keys = sample_dict.keys()
print("Keys:", keys)  # Output: dict_keys(['a', 'b', 'c'])

# Getting dictionary values
values = sample_dict.values()
print("Values:", values)  # Output: dict_values([1, 2, 3])

# Adding an item to the dictionary
sample_dict.update({'d': 4})
print("Updated Dictionary:", sample_dict)  # Output: {'a': 1, 'b': 2, 'c': 3, 'd': 4}

# Removing an item
removed_value = sample_dict.pop('b')
print("After pop('b'):", sample_dict)  # Output: {'a': 1, 'c': 3, 'd': 4}
print("Removed value:", removed_value)  # Output: 2

# Getting items (key-value pairs)
items = sample_dict.items()
print("Items:", items)  # Output: dict_items([('a', 1), ('c', 3), ('d', 4)])

# Clearing the dictionary
sample_dict.clear()
print("After clear():", sample_dict)  # Output: {}

#(ii) Concatenating Dictionaries

# Sample Dictionaries
dic1 = {1: 10, 2: 20}
dic2 = {3: 30, 4: 40}
dic3 = {5: 50, 6: 60}

# Method 1: Using dictionary unpacking
result = {**dic1, **dic2, **dic3}
print("Concatenated Dictionary (Method 1):", result)

# Method 2: Using a loop to update
result = {}
for d in (dic1, dic2, dic3):
    result.update(d)
print("Concatenated Dictionary (Method 2):", result)

#Exercise: List Comprehensions

#(i) List Comprehension for Lowercased Strings with Length Greater Than Five

# Sample List
sample_list = ["Python", "Java", "JavaScript", "HTML", "CSS", "Kotlin"]

# List comprehension: Lowercase strings with length > 5
result = [s.lower() for s in sample_list if len(s) > 5]
print("Lowercased strings with length > 5:", result)

#(ii) Removing Specific Elements by Index

# Sample List
sample_list = ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow', 'Teapink']

# Removing 0th, 4th, and 5th elements
result = [item for i, item in enumerate(sample_list) if i not in (0, 4, 5)]

print("List after removing specified elements:", result)

#Create a Python Program that perform with 10 tasks for any problem of your choice:

#Python Program: Student Grades Management System

# Task 1: Introduction
print("Welcome to the Student Grades Management System!")
print("This system allows you to manage student information including names and grades.")
print("You can add students, display their information, and manage grades.\n")

# Task 2: Terminal (Setup a terminal-like interface using a while loop)
def terminal():
    print("\n===== Main Menu =====")
    print("1. Add a Student")
    print("2. Show All Students")
    print("3. Update Student Grade")
    print("4. Exit")
    choice = input("Enter your choice (1-4): ")
    return choice

# Task 3: Python Interpreter (Handle the user input in real time)
# This is an interactive input (detailed later with lists).

# Task 4: Variables (Example of using variables)
students = []  # List to hold student details
# Each student will be a dictionary with 'name' and 'grade'.

# Task 5: Text Editor (Adding/editing data, such as adding a student)
def add_student():
    name = input("Enter student name: ")
    grade = input(f"Enter {name}'s grade: ")
    student = {'name': name, 'grade': grade}
    students.append(student)
    print(f"{name} has been added to the student list.\n")

# Task 6: Functions (Using functions for repeated tasks)
def show_all_students():
    if students:
        print("\nAll Students:")
        for student in students:
            print(f"Name: {student['name']}, Grade: {student['grade']}")
    else:
        print("No students available to display.\n")

# Task 7: Lists and Tuples (Using list for storing students, tuple for grades)
# We already used lists to store students as a dictionary.

# Task 8: Conditional Statements (Condition to check if a student exists or not)
def update_student_grade():
    name = input("Enter the name of the student whose grade you want to update: ")
    found = False
    for student in students:
        if student['name'].lower() == name.lower():
            new_grade = input(f"Enter the new grade for {name}: ")
            student['grade'] = new_grade
            print(f"{name}'s grade has been updated.\n")
            found = True
            break
    if not found:
        print(f"Student {name} not found.\n")

# Task 9: The For Loop (Iterating over students)
# We used for loops earlier when showing students.

# Task 10: User Input and the While Loop (Taking choices from the user and repeating tasks)
def main():
    while True:
        choice = terminal()  # Display the menu and get the choice
        if choice == '1':
            add_student()
        elif choice == '2':
            show_all_students()
        elif choice == '3':
            update_student_grade()
        elif choice == '4':
            print("Exiting the program. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

# Start the program
main()
