# Exercise 1 - Part I: Calculate the volume of a cube and categorize
height = float(input("Enter height (cm): "))
width = float(input("Enter width (cm): "))
depth = float(input("Enter depth (cm): "))

volume = height * width * depth

if 1 <= volume <= 10:
    label = "Extra Small"
elif 11 <= volume <= 25:
    label = "Small"
elif 26 <= volume <= 75:
    label = "Medium"
elif 76 <= volume <= 100:
    label = "Large"
elif 101 <= volume <= 250:
    label = "Extra Large"
else:
    label = "Extra-Extra Large"

print(f"Volume: {volume} cm³ - Category: {label}")

# Exercise 1 - Part II: Worker efficiency based on time taken
time_taken = float(input("Enter time taken (hours): "))
if 2 <= time_taken <= 3:
    print("Highly efficient")
elif 3 < time_taken <= 4:
    print("Needs to improve speed")
elif 4 < time_taken <= 5:
    print("Training required")
else:
    print("Worker has to leave")

# Exercise 1 - Part III: Username and password verification
username = input("Enter username: ")
password = input("Enter password: ")

correct_passwords = ["abc$123", "ABC$123"]

if password in correct_passwords:
    print("Welcome!")
else:
    print("I don't know you.")

# Exercise 2 - Part III: Various loop-based problems

# 1. List countries in a set
clist = ['Canada', 'USA', 'Mexico', 'Australia']
for country in clist:
    print(country)

# 2. Create a loop that counts from 0 to 100
for i in range(101):
    print(i)

# 3. Multiplication table
num = int(input("Enter a number for multiplication table: "))
for i in range(1, 11):
    print(f"{num} x {i} = {num * i}")

# 4. Output numbers 1 to 10 backwards
for i in range(10, 0, -1):
    print(i)

# 5. Count all even numbers to 10
for i in range(2, 11, 2):
    print(i)

# 6. Sum numbers from 100 to 200
total = sum(range(100, 201))
print("Sum from 100 to 200:", total)

# 7. List countries using while loop
clist = ["Canada", "USA", "Mexico"]
i = 0
while i < len(clist):
    print(clist[i])
    i += 1
