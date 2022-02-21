#We have imported random here for the random choice that will be taken by the computer
import random

while True:
    #We have taken the user input here
    user_input = input("Enter a choice (rock,paper,scissors): ")
    #These are the possible decisions taken by the computer and the user
    possible_actions = ['rock','paper','scissors']
    #Computer Decisions are imported with random for random choosing by the computer
    comp_input = random.choice(possible_actions)
    #Here the code will tell use what we have choose and what the computer has choose
    print(f"\nYou Choose - {user_input}\nComputer Choose - {comp_input}")

#Game decision
#Here if else is used to compute all the choices by the computer and the user    
    if user_input == comp_input:
        #These are the different choices that the user will make and if the user chooses the right option he will win the game.
        print("Both selected{user_input}, It's a tie")
    elif user_input == 'rock':
        if comp_input == 'scissors':
            print("Rock Smashes Scissors ! , You Win !")
        else:
            print("Paper covers rock ! , You Loose !")
    elif user_input == 'paper':
        if comp_input == 'rock':
            print("Paper covers rock ! , You Win !")
        elif comp_input == 'scissors':
            print("Scissors cuts paper !, You Loose !")
    elif user_input == 'scissors':
        if comp_input == 'rock':
            print("Rock beats Scissors ! , You Loose !")
        else:
            print("Scissors cuts paper ! , You Win !")
    break
