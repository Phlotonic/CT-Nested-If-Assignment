# Task 1: Code Correction You are provided with a Python 
# script that is supposed to help in event planning, but it 
# has errors. Identify and fix them.

# Buggy Code:

# attendees = input("Enter number of attendees: ")
# venue = "large hall" if attendees > 100 else "conference room"
# print(venue)

# Answer: Convert the string input into an integer
attendees = int(input("Enter number of attendees: "))
venue = "large hall" if attendees > 100 else "conference room"
print(venue)

# Task 2: Venue Selection

# Based on the corrected code from Task 1, further enhance 
# your code to recommend additional things like "audio system"
#  or "projector" based on the number of attendees.

# Answer:
attendees = int(input("Enter number of attendees: "))

if attendees > 100:
    venue = "large hall"
    additional_items = "audio system and projector"
elif attendees > 50:
    venue = "conference room"
    additional_items = "projector"
else:
    venue = "meeting room"
    additional_items = "none"

print(f"Venue: {venue}")
print(f"Additional items: {additional_items}")

# Task 3: Catering Choices

# Ask the user if they want "vegetarian" food. 
# Recommend "Veggie Delight Caterers" if yes, otherwise 
# recommend "Gourmet Meals Caterers".

# Answer: 
attendees = int(input("Enter number of attendees: "))

if attendees > 100:
    venue = "large hall"
    additional_items = "audio system and projector"
elif attendees > 50:
    venue = "conference room"
    additional_items = "projector"
else:
    venue = "meeting room"
    additional_items = "none"

print(f"Venue: {venue}")
print(f"Additional items: {additional_items}")

vegetarian = input("Do you want vegetarian food? (yes/no): ").strip().lower()

if vegetarian == "yes":
    caterer = "Veggie Delight Caterers"
else:
    caterer = "Gourmet Meals Caterers"

print(f"Caterer: {caterer}")
