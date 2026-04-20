# Exercise , NUMBER GUESSING GAME
# Make a variable ,like winning_number and assign it a number. 
# Ask the user to guess the winning number. 
# If the user guesses the winning number, print "Congratulations! You guessed the winning number." Otherwise, print "Sorry, that's not the winning number. Try again!".

# google :how to generate random number in python
import random
winning_number = random.randint(1, 100)  # generates a random number between 1 and 100
print(winning_number);
guess=int(input("Guess the winning number between 1 and 100: "));
if guess==winning_number:
    print("Congratulations! You guessed the winning number.");
else:
    if guess<winning_number:
        print("Sorry, that's not the winning number. Try again! Your guess is too low.");
    else:
        print("Sorry, that's not the winning number. Try again! Your guess is too high.");  
print("Thank you for playing the number guessing game! The winning number was:", winning_number);