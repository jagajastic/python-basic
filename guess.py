import random

guess = int(input("What's your guess?: "))

correct_number = random.randint(1,13);
guess_count = 1

while guess != correct_number:
  guess_count +=1
  guess = int(input("What's your guess?: "))


print(f"Congrats! The right answer was {correct_number}. it took you {guess_count} guesses.")