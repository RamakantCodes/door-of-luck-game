haunted treasure door / door of luck
import random

print("welcome to door of luck") 
print("you are in a room with 3 doors one will help you escape and others may trap you")
correct_door=random.randint(1,3)

choice = int(input("choose a door (1, 2, or 3): "))

if choice == correct_door:
    print("Congratulations! You found the correct door and escaped!")       

elif choice == 1 or choice == 2 or choice == 3:
    print("Sorry, that's not the correct door. You've been trapped!") 

else:
    print("Invalid choice. Please choose a door number between 1 and 3.") 

print("computer generated correct door was: ", correct_door)   
