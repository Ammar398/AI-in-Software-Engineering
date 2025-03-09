# Exercise 1 - I: Square and cube every number in a given list using Lambda
numbers = [1, 2, 3, 4, 5]
square = list(map(lambda x: x ** 2, numbers))
cube = list(map(lambda x: x ** 3, numbers))
print("Squares:", square)
print("Cubes:", cube)

# Exercise 1 - II: Check if a string starts with a given character using Lambda
starts_with = lambda string, char: string.startswith(char)
print(starts_with("Hello", "H"))  # True

# Exercise 1 - III: Extract year, month, date, and time using Lambda
from datetime import datetime
now = datetime.now()
get_year = lambda dt: dt.year
get_month = lambda dt: dt.month
get_day = lambda dt: dt.day
get_time = lambda dt: dt.strftime("%H:%M:%S")
print("Year:", get_year(now))
print("Month:", get_month(now))
print("Day:", get_day(now))
print("Time:", get_time(now))

# Exercise 2 - I: Store city details in a file
with open("cities.txt", "w") as file:
    while True:
        city = input("Enter city name (or 'done' to stop): ")
        if city.lower() == 'done':
            break
        population = input("Enter population: ")
        mayor = input("Enter mayor: ")
        file.write(f"{city}, {population}, {mayor}\n")

# Exercise 2 - II: Append text to a file
with open("student.txt", "a") as file:
    file.write("Now we are AI students\n")

# Exercise 3: Using Python modules
import math, random, time
print("Square root of 16:", math.sqrt(16))
print("Random number between 1 and 10:", random.randint(1, 10))
time.sleep(1)  # Pauses for 1 second
print("Current time:", time.ctime())
