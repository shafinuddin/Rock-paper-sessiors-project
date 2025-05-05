import random

rock ="""
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
"""

# Paper
paper="""
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
"""

# Scissors
sessiors="""
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""
game_image=[rock,paper,sessiors]
# Rock Paper Scissors ASCII Art
print("Welcome to Rock, Paper, Scissors!")
print("To playthis game you need to choose one of the following options:")
print("0. Rock")
print("1. Paper")
print("2. Scissors")
user_choice = int(input("Enter your choice (0, 1, or 2): "))
print("You chose:")
print(game_image[user_choice])
computer_choice = random.randint(0, 2)
print("Computer chose:")
print(game_image[computer_choice])
if user_choice >=2 or user_choice <0:
    print("Invalid choice. Please try again.")
elif user_choice == 0 and computer_choice == 2:
    print("You win!")
elif user_choice > computer_choice:
    print("You win!")
elif user_choice < computer_choice:
    print("You lose!")
elif user_choice == computer_choice:
    print("It's a draw!")

