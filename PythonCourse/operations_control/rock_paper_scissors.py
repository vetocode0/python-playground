import random

computer_choice = random.choice(['rock','paper','scissors'])
user_choice = input("Do you want to play rock, paper, or scissors?\n")

print("Computer choice: ", computer_choice)

if computer_choice == user_choice:
    print("It's a draw")
elif user_choice == "rock" and computer_choice == "scissors":
    print("You win! Great job!")
elif user_choice == "paper" and computer_choice == "rock":
    print("You win! Great job!")
elif user_choice == "scissors" and computer_choice == "paper":
    print("You win! Great job!")
else:
    print("You lose. Better luck next time.")