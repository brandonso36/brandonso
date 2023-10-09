import random

user_input = input("Enter rock, paper, or scissors: ")
ai_number = random.randint(1, 3)

def win_lose():
    if user_input == "rock" and ai_number == 3:
        print("You chose rock. You win!")
    elif  user_input == "rock" and ai_number == 2:
        print("You chose rock. You lose!")
    elif  user_input == "rock" and ai_number == 1:
        print("You chose rock. It's a tie!")
    elif user_input == "paper" and ai_number == 2:
        print("You chose paper. It's a tie")
    elif  user_input == "paper" and ai_number == 3:
        print("You chose paper. You lose")
    elif user_input == "paper" and ai_number == 1:
        print("You chose paper. You win")
    elif user_input == "scissors" and ai_number == 1:
        print("You chose scissors. You lose!")
    elif user_input == "scissors" and ai_number == 2:
        print("You chose scissors. You win!")
    elif user_input == "scissors" and ai_number == 3:
        print("You chose scissors. It's a tie!")
    else: 
        print("Enter a valid input")
        exit()

def ai_choice():
    if ai_number == 1:
        print("AI chose Rock!")
    elif ai_number == 2:
        print("AI chose Paper!")
    elif ai_number == 3:
        print("AI chose Scissors!")
    
win_lose()
ai_choice()