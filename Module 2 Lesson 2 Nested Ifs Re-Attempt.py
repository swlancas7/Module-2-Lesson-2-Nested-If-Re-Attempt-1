echo "# Module-2-Lesson-2-Nested-If-Re-Attempt" >> README.md
git init
git add README.md
git commit -m "first commit"
git branch -M main
git remote add origin https://github.com/swlancas7/Module-2-Lesson-2-Nested-If-Re-Attempt.git
git push -u origin main

#Nested Decisions: The Adventure Game: Buggy Code Correction
place = input("Choose a place: forest or cave?")

if place == "forest":
    action = input("climb a tree or cross a river?")
    if action == "climb a tree":
        print("You found a bird's nest!")
    elif action == "cross a river":
        print("You found a boat!")
else:
    print("You find a hidden treasure!")

#Setting The Scene
place = input("Choose a place: forest or cave?")

if place == "forest":
    action = input("climb a tree or cross a river?")
    if action == "climb a tree":
        print("You found a bird's nest!")
    elif action == "cross a river":
        print("You found a boat!")
else 
    print("You find a hidden treasure!")

    action = input("light a torch or proceed in the dark?")
    if action == "light a torch"
        print ("Make way through cave.")
    elif action == "proceed in the dark"
        print ("Trip and fall into bat guano.")

#Default Path
place = input("Choose a place: forest or cave?")

if place == "forest":
    action = input("climb a tree or cross a river?")
    if action == "climb a tree":
        print("You found a bird's nest!")
    elif action == "cross a river":
        print("You found a boat!")
elif place == "cave":
    action = input("light a torch or proceed in the dark?")
    if action == "light a torch"
        print ("Make way through cave.")
    elif action == "proceed in the dark"
        print ("Trip and fall into bat guano.")
else:
    pass  # Nothing


#Quick Decisions: The Event Planner: Code Correction
attendees = input("Enter the number of attendees:")
attendees = int(attendees)
venue = "large hall" 
if attendees > 100 
else
    print("conference room")

#Venue Selection
attendees = input("Enter the number of attendees:")
attendees = int(attendees)
venue = "large hall" 
if attendees > 100
equipment = input ("equipment type")
equipment = "audio system"
if attendees > 100
else 
    print("projector")

#Catering Choices
attendees = input("Enter the number of attendees:")
attendees = int(attendees)
venue = "large hall" 
if attendees > 100
equipment = input ("equipment type")
equipment = "audio system"
if attendees > 100
else 
    print("projector")
vegetarianoption = input("Vegetarian or not.")
vegetarianoption = "Veggie Delight Caterers"
if vegetarianoption == "Yes."
else 
    print("Gourmet Meal Caterers")