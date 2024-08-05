# Task 1: Code Correction 
# You are provided with a Python script that is supposed to guide a user 
# through an adventure game, but it has some errors. Identify and fix them.

# Buggy Code:

# place = input("Choose a place: forest or cave? ")

# if place = "forest":
#    action = input("climb a tree or cross a river?")
#    if action = "climb a tree":
#        print("You found a bird's nest!")
#    else action = "cross a river":
#        print("You found a boat!")
# elif place = "cave":
#    print("You find a hidden treasure!")

# Answer:
place = input("Choose a place: forest or cave? ")

if place == "forest": # Use == for comparison instead of = in the if statements.
    action = input("climb a tree or cross a river? ")
    if action == "climb a tree":
        print("You found a bird's nest!")
    elif action == "cross a river": # Use elif instead of else for the second condition inside the nested if.
        print("You found a boat!")
elif place == "cave": 
    print("You find a hidden treasure!")

# Task 2: Setting the Scene
# Based on your corrected code from Task 1, expand the game. 
# If the user chooses "cave", ask them if they want to 
# "light a torch" or "proceed in the dark", and provide 
# outcomes for each decision.

# Answer:
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
        print("You find a hidden treasure!")
    elif action == "proceed in the dark":
        print("You stumble and fall, but discover a hidden passage!")

# Task 3: Default Path
# If the user makes an invalid choice at any point, 
# incorporate a pass statement to handle it.

# Answer: 
place = input("Choose a place: forest or cave? ")

if place == "forest":
    action = input("climb a tree or cross a river? ")
    if action == "climb a tree":
        print("You found a bird's nest!")
    elif action == "cross a river":
        print("You found a boat!")
    else:
        pass  # Handle invalid action
elif place == "cave":
    action = input("light a torch or proceed in the dark? ")
    if action == "light a torch":
        print("You find a hidden treasure!")
    elif action == "proceed in the dark":
        print("You stumble and fall, but discover a hidden passage!")
    else:
        pass  # Handle invalid action
else:
    pass  # Handle invalid place
