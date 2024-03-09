import math
import random

place = input("Choose a place: forest or cave? ")

if place == "forest":
    action = input("climb a tree or cross a river?")
    if action == "climb a tree":
        print("You found a bird's nest!")
    elif action == "cross a river":
        print("You found a boat!")
elif place == "cave":
    print("You find a hidden treasure!")

place = input("Choose a place: forest or cave? ")

if place == "forest":
    action = input("climb a tree or cross a river? ")
    if action == "climb a tree":
        print("You found a bird's nest!")
    elif action == "cross a river":
        print("You found a boat!")
elif place == "cave":
    action = input("light a torch or proceed in the dark? ")
    if action == "light a torch":
        print("Enjoy some smores!")
    elif action == "proceed in the dark":
        print("Run as fast as you can!")

# Task Three: Default Path
place = input("Choose a place: forest or cave? ")

if not place == "forest" and not place == "cave":
    pass
if place == "forest":
    action = input("climb a tree or cross a river? ")
    if action == "climb a tree":
        print("You found a bird's nest!")
    elif action == "cross a river":
        print("You found a boat!")
    elif not action == "climb a tree" and not action == "cross a river":
        pass
elif place == "cave":
    action = input("light a torch or proceed in the dark? ")
    if action == "light a torch":
        print("Enjoy some smores!")
    elif action == "proceed in the dark":
        print("Run as fast as you can!")
    elif not action == "light a torch" and not action == "proceed in the dark":
        pass

# Quick Decisions: The Event Planner

attendees = int(input("Enter number of attendees: "))
venue = "large hall" if attendees > 100 else "conference room" 
print(venue)

# Task Two: Venue Selection 

attendees = int(input("Enter number of attendees: "))
if attendees > 100:
    venue = "Large hall"
    if venue == "Large hall":
        print(venue, ": Audio system recommended!")
else:
    venue = "Conference room"
    if venue == "Conference room":
        print(venue, ": Projector recommended!")

# Task Three: Catering Choices

answer = input("Do you want vegetarian food: ")
print("Veggie Delight Caterers recommended!") if answer == "yes" else print("Gourmet Meals Caterers recommended!")

# Task Three: Silent Failures: The Error Handler 
# Task One Correction:
try:
    x = 1 / 0
except ZeroDivisionError:
    pass
# Task Two Division Calculator
try:
    x = 1 / 0
except ZeroDivisionError:
    pass
try:
    y = 2 / "test_string"
    print(y)
except TypeError:
    pass
try:
    z = math.sqrt(-20)/2
    print(z)
except ValueError:
    pass

#Task Three: File Reader
path = input("Input path to file: ")

try:
    file = open(path, 'r')
    details = file.read()
    file.close()
    print(details)
except FileNotFoundError:
    pass

# Task Four: Nested Quick Decisions: The Shopping Assistant
# Task One: Code Correction
weather = input("Enter the weather: sunny, rainy, or cold: ")
clothing = "sunglasses" if weather == "sunny" else "umbrella" \
    if weather == "rainy" else "sweater"
print(clothing)

# Task Two: Clothing Recommendation 
weather = input("Enter the weather: sunny, snowy, rainy, chilly or cold: ")
clothing = "sunglasses" if weather == "sunny" else "boots" \
    if weather == "snowy" else "umbrella" if weather == "rainy" else "hat" \
         if weather == "chilly" else "sweater" 
print(clothing)

# Task Three: Accessory Recommendation
weather = input("Enter the weather: sunny, snowy, rainy, chilly or cold: ")
clothing = "Sunglasses" if weather == "sunny" else "Boots" if weather == "snowy"\
     else "Umbrella" if weather == "rainy" else "hat" \
        if weather == "chilly" else "Sweater" 
print("Clothing Based on Weather:" , clothing)
accessory = "Go barefoot!" if clothing == "sunglasses" else "Wear matching belt!"\
     if clothing == "boots" else "Wear bright raincoat or pancho!" \
        if clothing == "umbrella" else "Wear your hair down!"\
             if clothing == "hat" else "Wear jeans!"
print("Recommendation:", accessory)

# Task Five: The Silent Logger: System Monitor
# Task One: Code Correction 

cpu_usage = random.randint(0, 100)
if cpu_usage > 90:
    print("High CPU usage!")
elif cpu_usage > 80 and cpu_usage <= 90:
    pass

# Task Two: System Check

cpu_usage = random.randint(0, 100)
memory_usage = random.randint(6,8)
disk_space = random.randint(400, 600)

print("System check...")

if cpu_usage > 90:
    print(cpu_usage, "GB being used -","Status: High CPU usage!")
    if disk_space == 400:
        print(disk_space, "GB being used -","Inching toward capacity!")
    elif(disk_space > 400 and disk_space <= 550):
        print(disk_space, "GB being used -","Status: Consider deleting some files..")
        if(memory_usage == 5):
            print(memory_usage, "GB being used -","Status: Normal usage!")
        elif(memory_usage > 7):
            print(memory_usage, "GB being used -","Status: Close some processes!")
elif cpu_usage > 80 and cpu_usage <= 90:
    print(cpu_usage, "GB being used -","Status: Typical CPU usage!")
else:
    print("Good Condition!")

#Task Three: Alert System
cpu_usage = random.randint(0, 100)
memory_usage = random.randint(6,8)
disk_space = random.randint(400, 600)
print("System check...")

if cpu_usage > 90:
    print(cpu_usage, "GB being used -","Status: High CPU usage!")
    if disk_space == 400:
        pass
    elif(disk_space > 490 and disk_space <= 550):
        print(disk_space, "GB being used -","Status: Consider deleting some files..")
    if(memory_usage == 5):
        pass
    elif(memory_usage > 7):
            print(memory_usage, "GB being used -","Status: Close some processes!")
elif cpu_usage > 80 and cpu_usage <= 90:
    pass
else:
    print("Good condition!")
