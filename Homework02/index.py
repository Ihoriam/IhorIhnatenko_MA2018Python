# imoport modules
import simplegui as sg
import random
import math

# settings of the game
secret_number = 0
range_number = 100
num_guesses = 7


def input_guess(guess):
    """Compare secret number with users guess"""
    user_guess = int(guess)
    print ("\nGuess was: " + str(guess))
    if user_guess == secret_number:
        print ("You win!")
        new_game()
    elif user_guess > secret_number:
        decrement_guesses()
        print ("Lower!")
    elif user_guess < secret_number:
        decrement_guesses()
        print ("Higher!")
    else:
        print ("Ops... Something goes wrong ")


def new_game():
    """Start the game"""
    global secret_number, num_guesses
    # change number of guesses
    if range_number == 100:
        num_guesses = 7
    elif range_number == 1000:
        num_guesses = 10
    # create random number in range
    secret_number = random.randint(0, range_number)
    print("\nGame started!")
    print("Guess the number in the range from 0 to " + str(range_number))
    print("Number of remaining guesses is " + str(num_guesses))


def range100():
    """Change range of numbers"""
    global range_number
    range_number = 100
    print("\nEasy mod - on")
    new_game()


def range1000():
    """Changes range of numbers and number of guesses"""
    global range_number, num_guesses
    range_number = 1000
    print("\nHard mod - on")
    new_game()


def decrement_guesses():
    """Decrement number of guesses with each wrong step"""
    global num_guesses
    num_guesses -= 1
    if num_guesses > 0:
        print("Remaining guesses: " + str(num_guesses))
    else:
        print("You lose! The number was " + str(secret_number))
        new_game()


def restart_game():
    """Restart the game and reset settings"""
    global range_number, num_guesses
    range_number = 100
    num_guesses = 7
    print("Restarting game...")
    new_game()


# creat frame
frame = sg.create_frame("Guess the number", 300, 300)

# register event handlers for control elements
frame.add_input("Enter guess: ", input_guess, 50)
frame.add_button("Range is (0, 100]", range100, 200)
frame.add_button("Range is (0, 1000]", range1000, 200)
frame.add_button("Restart", restart_game, 200)

# start frame and game
frame.start()
new_game()

