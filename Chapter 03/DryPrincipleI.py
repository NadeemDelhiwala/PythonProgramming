# Game
import random
winning_number = 43;
guess_count = 1;
game_over = False

while True:
  num = int(input("Guess a number between 1 and 100 : "));

  if num == winning_number:
    print(f"you win, and you guessed this number in  {guess_count} times")
    break
  else:
    if num < winning_number:
      print(f"Too low")

    else:
      print(f"Too High")
  guess_count += 1
  continue

