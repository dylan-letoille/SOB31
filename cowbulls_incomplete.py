import random


def compare_numbers(numbers, user_guess):
    cowbull = [0, 0]  # cowbull list for displaying cows and bulls

    for i in range(4):  # loops through the 4 digits and compares them to the number
        if user_guess[i] == numbers[i]:  # adds 1 to bull if number matches position and value
            cowbull[1] += 1
        elif user_guess[i] in numbers:  # adds 1 to cow if number matches value
            cowbull[0] += 1

    return cowbull


playing = True  # gotta play the game
number = str(random.randint(1000, 9999))  # random 4-digit number  (replaced 1 with 1000)
guesses = 0
# print(number) Added parenthesis around number and commented it out for the real game

print("Let's play a game of Cowbull!")  # explanation
print("I will generate a number, and you have to guess the numbers one digit at a time.")
print("For every number that exists in the sequence but is in wrong place, you get a cow. For every one in the right "
      "place, you get a bull.")  # new line for clarity
print("The game ends when you get 4 bulls!")
print("Type exit at any prompt to exit.")

while playing:
    user_guesses = input("Give me your best guess!")  # removed raw_
    if user_guesses == "exit":
        print("ok, the number was", number, "see you next time")  # displays the number before exiting (something extra)
        break
    while not user_guesses.isdigit() or len(user_guesses) != 4:  # checks for errors in inputting
        user_guesses = input("please enter a valid 4 digit number")
    cowbullcount = compare_numbers(number, user_guesses)  # calls cowbullcount function
    guesses += 1  # tracks guesses

    print("You have " + str(cowbullcount[0]) + " cows, and " + str(cowbullcount[1]) + " bulls.")

    if cowbullcount[1] == 4:
        playing = False
        print("You win the game after " + str(guesses) + "! The number was " + str(number))
        break  # redundant exit
    else:
        print("Your guess isn't quite right, try again.")
