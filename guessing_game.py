"""
Alan Wood
Python Web Development Techdegree
Project 1 - Number Guessing Game
--------------------------------
"""

import random as rand

def start_game():
    # Welcome the user
    print("------------------------------------")
    print("Welcome to the Number Guessing Game!")
    print("------------------------------------")

    # Generate random number
    random_number = rand.randint(1, 10)

    # Variable for controlling the overall loop
    bool_exit = False

    # Variables for controlling play through
    is_first_turn = True
    showed_high_score = False
    play_again = False

    # Variables for keeping track of high score and
    # number of tries
    number_of_tries = 0
    high_score = 0

    while bool_exit == False:
        # If it is the first turn and the high score hasnt been shown
        # then the high score will not be shown otherwise it will
        if is_first_turn == False and showed_high_score == False:
            if number_of_tries < high_score or high_score == 0:
                high_score = number_of_tries
            print("Your high score is {}.".format(high_score))
            number_of_tries = 0
            showed_high_score = True
        # Requests a number from the user and changes it to an int for comparison
        guess = int(input("Choose a number between 1 and 10: "))
        # Checks to make sure the guess is within range
        # if not then the user is prompted to fix it
        if guess > 10 or guess < 1:
            print("Please choose a number between 1 and 10.")
            continue
        # Checks the guess against the random number
        if guess == random_number:
            # Number of tries is incremented by one
            number_of_tries += 1
            # Show user they are correct and the number of tries it took
            print("That is correct! It took you {} tries!".format(number_of_tries))
            # Loop continues until the user chooses to play again or not
            while play_again == False:
                # Prompts user for an answer to play again or not
                try_again = input("Would you like to play again? (y)es or (n)o: ")
                # If the user chooses Y or y then they play again
                if try_again == "y" or try_again == "Y":
                    play_again = True
                    is_first_turn = False
                    showed_high_score = False
                    random_number = rand.randint(1, 10)
                # If the user chooses N or n then the game is over
                elif try_again == "n" or try_again == "N":
                    # play_again is set to True in order to break the loop
                    play_again = True
                    # bool_exit is set to True to break the containing loop
                    # and exiting the game
                    bool_exit = True
                # If the user chooses a value that is not Y,y,N,n then they are prompted to do so
                else:
                    print("Please choose either y for yes or n for no.")
                    continue
            # Resets play_again value to False for next time
            play_again = False
            # Continues the loop to continue asking for guesses
            continue
        # If the guess is not correct
        else:
            # If the guess is less than the random number
            # prompt user to choose a higher number
            if guess < random_number:
                print("Incorrect.  The number is higher.")
                number_of_tries += 1
            # If the guess is less than the random number
            # prompt user to choose a lower number
            else:
                print("Incorrect.  The number is lower.")
                number_of_tries += 1

    # Signal the end of the game
    print("Thanks for playing!")


if __name__ == '__main__':
    # Kick off the program by calling the start_game function.
    start_game()
