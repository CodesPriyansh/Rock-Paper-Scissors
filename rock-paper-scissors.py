import random
print("WELCOME TO PyPlays")
print("Let's play Rock🪨 Paper📃 Scissors ✂️")
game_list = ["rock", "paper", "scissors"]
user_choice = input("Pick spmething: rock, paper or scissors.")
computer_choice = random.choice(game_list)

if user_choice == "rock" and computer_choice == "rock":
    print(f"draw, computer choice:{computer_choice}")
elif user_choice == "paper" and computer_choice == "paper":
    print(f"draw, computer choice:{computer_choice}")
elif user_choice == "scissors" and computer_choice == "scissors":
    print(f"draw, computer choice:{computer_choice}")
elif user_choice == "rock" and computer_choice == "paper":
    print(f"you lose, computer choice:{computer_choice}")
elif user_choice == "paper" and computer_choice == "scissors":
    print(f"you lose, computer choice:{computer_choice}")
elif user_choice == "scissors" and computer_choice == "rock":
    print(f"you lose, computer choice:{computer_choice}")
else:
    print(f"you win, computer choice:{computer_choice}")