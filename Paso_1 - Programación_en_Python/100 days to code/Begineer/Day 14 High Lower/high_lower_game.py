import random
from game_data import data
from art import logo, vs

def lose(wins):
    """It is printed when the user loses"""
    print("\n" * 15)
    print(logo)
    if wins == 0:
        print("don't give up, try again")
    else:
        print(f"Sorry, that's wrong- Final score: {wins}")

def game_higher_lower():
    """There is all the code for you to play higher lower"""
    random_a = random.choice(data)
    num_wins = 0
    while True:
        print(logo)
        random_b = random.choice(data)
        if random_b == random_a:
            while random_a == random_b:
                random_b = random.choice(data)
        if num_wins > 0:
            print(f"You're right! Current score: {num_wins}.")
        print(f"Compare A: {random_a['name']}, a {random_a['description']}, from {random_a['country']}.")
        print(vs)
        print(f"Against B: {random_b['name']}, a {random_b['description']}, from {random_b['country']}.")
        guess = input("Who has more followers? Type 'A' or 'B':  ").upper()
        while guess not in ("A", "B"):
            print("Please, type a correct option")
            guess = input("Who has more followers? Type 'A' or 'B':  ").upper()
        if random_a["follower_count"] > random_b["follower_count"]:
            if guess == 'A':
                random_a = random_b
                num_wins += 1
                print("\n" * 20)
            else:
                lose(num_wins)
                return
        else:
            if guess == 'A':
                lose(num_wins)
                return
            else:
                random_a = random_b
                num_wins += 1
                print("\n" * 20)

game_higher_lower()
try_again = 'y'
while try_again in ('y', 'n'):
    try_again = input("Do you want play again? Type 'y' or 'n'.").lower()
    if try_again == 'y':
        print("\n" * 20)
        game_higher_lower()
    elif try_again == 'n':
        print("End of the game.")
        break
    else:
        print("Type a valid answer.")


