import random 

name = input('Enter your name')
print(f"Welcome {name} to Rock, Paper, Scissors!!! Let's play the game")


def game():
    computer_choice = random.choice(['rock', 'paper', 'scissors'])
    player_choice = input("Enter rock, paper, scissors: ").lower()
    
    if player_choice == computer_choice:
        print("It is a Tie!")
    elif (player_choice == 'rock' and computer_choice == 'scissors') or \
        (player_choice == 'scissors' and computer_choice == 'paper') or \
        (player_choice == 'paper' and computer_choice == 'rock'):
        return "You Win!"
    else:
        return "Computer Wins!"

game ()

   
#Rock beats Scissors (Rock crushes Scissors).
#Scissors beats Paper (Scissors cuts Paper).
#Paper beats Rock (Paper covers Rock).


