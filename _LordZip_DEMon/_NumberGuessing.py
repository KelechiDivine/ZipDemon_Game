import random

# the default set of guesstaken to zero
guess_taken= 0

# recieve user input and save in a variable

name= input("Hello buddy! What is your name: ")

# create another variable called number, let the variable store the random number
# the range of the random number will be set between 1-20 here because we don't wanna deal
# with too many large numbers and mainly because of memory space

number= random.randint(1, 8)

# create a place holder that stores the user name
# print a message with the user name on it that tells them what to do next
place_holder="{}".format(name)
print(f"Well, {place_holder} I am thinking of a number between 1-20." )


# a for loop that allows user guess at most six times
for guess_taken in range(6):
    guess= int(input(place_holder + " please take a guess: "))
    print(guess)
    
    # create an if statement that checks if our guesstaken is lower or
    # greater than the number expected
    if guess < number:
        print("Dear, " + place_holder + "!" + " your guess is too low!")
    
    if guess > number:
        print("Dear, " + place_holder + " your guess is too high.")
        
    if guess == number:
        print("Hiippiee..." + place_holder + " you've just got the number I am thinking off.")
        break

# create another if statement outside the for loop
# that check and validates the user input
if guess == number:
    guess_taken= str(guess_taken + 1)
    print("Good job, " + place_holder +  "!" + " you guessed my number in " + guess_taken
           + " guesses!")
    
if guess != number:
    number= str(number)
    print("Nope. The number I was thinking of was " + number + ".")
