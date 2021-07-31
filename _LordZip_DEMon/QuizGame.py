import time

true = ["T", "t", "True"]
false = ["F", "f", "False"]
correct = 0  # Storing the correct answers

name = input("What's your name? ")  # Storing the user's name

print(
"\nOK, " + name + ", let's get started. Remember, the following answers are only True or False.")
time.sleep(2)

print("\nParis is the captial of France.")
user_choice = input(">>> ")

if user_choice in true:
    user_choice = user_choice + 1  # If correct, the user gets one point

else:
    correct = correct + 0

print("\nEngland is an island.")

user_choice = input(">>> ")

if user_choice in false:
    user_choice = user_choice + 1

else:
    correct = correct + 0

print("\nNorthern Ireland isn't part of Great Britian.")

user_choice = input(">>> ")

if user_choice in false:
    correct = correct +  1

else:
    correct = correct + 0

print("\nAndorra is between France and Spain.")

user_choice = input(">>> ")

if user_choice in true:
    correct = correct + 1
else:
    correct = correct + 0

print("\nIran use to be part of the Perisan Empire.")

user_choice = input(">>> ")

if user_choice in true:
    correct = correct + 1

else:
    correct = correct + 0

print("\nTurkmenistan isn't a real country.")

user_choice = input(">>> ")

if user_choice in false:
    correct = correct +  1

else:
    correct = correct + 0

print(
"\nYou're finished, " + name + ". You got", correct, "out of 6 correct.")