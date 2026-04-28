# Game
import random
winning_number = 43;
guess_count = 1;
num = int(input("Guess a number between 1 and 100"));
game_over = False

while not game_over:
  if num == winning_number:
    print(f"you win, and you guessed this number in  {guess_count} times")
    game_over = True
  else:
    if num < winning_number:
      print(f"Too low")
      guess_count += 1
      num = int(input("Guess a number between 1 and 100"));

    else:
      print(f"Too High")
      guess_count += 1
      num = int(input("Guess a number between 1 and 100"));

