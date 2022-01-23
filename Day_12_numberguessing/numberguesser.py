#Number Guessing Game Objectives:

# Include an ASCII art logo.
# Allow the player to submit a guess for a number between 1 and 100.
# Check user's guess against actual answer. Print "Too high." or "Too low." depending on the user's answer. 
# If they got the answer correct, show the actual answer to the player.
# Track the number of turns remaining.
# If they run out of turns, provide feedback to the player. 
# Include two different difficulty levels (e.g., 10 guesses in easy mode, only 5 guesses in hard mode).
import random
from art import logo
def check_guess(guess, answer, lives):
  if guess < answer:
    print("Too low.\nGuess again.")
    return lives - 1
  elif guess > answer:
    print("Too high.\nGuess again.")
    return lives - 1
  else:
    print(f"You got it! The answer was {answer}.")

def check_difficulty(difficulty):
  if difficulty == 'easy':
    lives = 10
    print(f"You have {lives} attempts remaining to guess the number.")
    return lives
  elif difficulty == 'hard':
    lives = 5
    print(f"You have {lives} attempts remaining to guess the number.")
    return lives

def update_lives(lives):
  print(f"You have {lives} attempts remaining to guess the number.")


def game():
  print(logo)
  print("Welcome to the Number Guessing Game!")
  print("I'm thinking of a number between 1 and 100.")
  answer = random.randint(1, 100)
  print(f"Pssst, the correct answer is {answer}.")
  difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ")
  
  # Game code
  
  lives = check_difficulty(difficulty)
  game_running = True
  
  guess = 0
  while guess != answer:
    guess = int(input("Make a guess: "))
    # Check guess
    lives = check_guess(guess, answer, lives)
    update_lives(lives)
    if lives == 0:
      print("You've run out of guesses, you lose.")
      break

game()