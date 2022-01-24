from art import logo, vs
from game_data import data
from random import randint


def random_account():
    return data[randint(1, len(data))]


def compare_account(account_1, account_2):
    if account_1['follower_count'] > account_2['follower_count']:
        return 'A'
    else:
        return 'B'


def update(account_1, account_2):
    print(f"Compare A: {account_1['name']}, a {account_1['description']}, from {account_1['country']}.")
    print(vs)
    print(f"Against B: {account_2['name']}, a {account_2['description']}, from {account_2['country']}.")


def check_guess(guess, winner, score):
    if guess == winner:
        print(f"You're right!")
        return False
    else:
        print(f"Sorry, thats wrong.")
        return True


def update_score(game_over, score):
    if game_over == False:
        score += 1
        print(f"Current score: {score}")
        return score
    else:
        print(f"Final score: {score}")


def game():
    score = 0
    game_over = False
    print(logo)
    account_1 = random_account()
    while not game_over:
        account_2 = random_account()
        winner = compare_account(account_1, account_2)
        update(account_1, account_2)
        guess = input("Who has more followers? Type 'A' or 'B': ")
        game_over = check_guess(guess, winner, score)
        score = update_score(game_over, score)
        if winner == 'B':
            account_1 = account_2


game()
