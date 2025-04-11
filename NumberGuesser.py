import random 

name = input('Enter your name')
print(f"Welcome {name} to Number Guess Game!!! You've got 3 attempts!")
computer_guess = random.randint(1,100) #generates random number
attempts = 3
#user_guess = int(input("Guess a number from 1 to 100: "))
secret_number = computer_guess


def game():
    for attempt in range(attempts):
        user_guess = int(input("Guess a number from 1 to 100: "))
        if user_guess == computer_guess:
            print(f"Congratulations {name}! You guessed right")
            return "End of the Game"
        elif user_guess < computer_guess:
            print("Too low! Try again.")
        else:
            print("Too high! Try again.")
        remaining_attempts = attempts - (attempt +1)
        if remaining_attempts > 0:
            print(f"{remaining_attempts} attempt(s) left")
        else:
            print(f"Sorry {name}, you've got 0 attempt left")
    #except ValueError:
        #print("Invalid input! Please enter a valid number")


game ()


