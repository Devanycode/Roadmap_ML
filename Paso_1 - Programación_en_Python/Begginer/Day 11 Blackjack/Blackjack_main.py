import random
from art import logo

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
def blackjack_full_game():
    def shuffle():
        return [random.choice(cards) for card in range(0, 2)]

    def final_score(mallet):
        score = sum(mallet)
        aces = mallet.count(11)
        while score > 21 and aces > 0:
            score -= 10
            aces -= 1
        return score

    def final_hands():
        print(f"Your final hand: {user_cards} final score: {final_score(user_cards)}.")
        print(f"Computer's final hand: {computer_cards} final score: {final_score(computer_cards)}.")

    def blackjack_print():
        print(f"Your cards: {user_cards}, current score: {final_score(user_cards)}.")
        print(f"Computer's first card: {computer_first_card}.")

    def continue_taking_cards():
        while True:
            take_card = input("Type 'y' to get another card, type 'n' to pass: ")
            if take_card == 'y':
                user_cards.append(random.choice(cards))
                user_score = final_score(user_cards)
                if user_score > 21:
                    final_hands()
                    print("You went over. You Lose. 😤")
                    return
                blackjack_print()
            elif take_card == 'n':
                blackjack_results()
                return
            else:
                print("Invalid input. Please type 'y' or 'n'.")

    def blackjack_results():
        computer_score = final_score(computer_cards)
        while computer_score < 17:
            computer_cards.append(random.choice(cards))
            computer_score = final_score(computer_cards)
        final_hands()
        user_score = final_score(user_cards)
        if computer_score > 21:
            print("Opponent went over. You Win. 😁")
        elif computer_score > user_score:
            print("You Lose. 😤")
        elif computer_score < user_score:
            print("You Win. 😎")
        else:
            print("The match was a Draw. 🙃")
        return

    print("\n"*20)
    print(logo)
    user_cards = shuffle()
    computer_cards = shuffle()
    user_score = final_score(user_cards)
    computer_score = final_score(computer_cards)
    if len(user_cards) == 2 and len(computer_cards) ==2:
        if user_score == 21 and computer_score < 21:
            final_hands()
            print("Blackjack! You Win. 😎")
            return
        elif computer_score == 21 and user_score < 21:
            final_hands()
            print("Blackjack! You Lose. 😤")
            return
        elif computer_score == 21 and user_score == 21:
            final_hands()
            print("Double Blackjack! he match was a Draw. 🙃")
            return
    computer_first_card = computer_cards[0]
    blackjack_print()
    continue_taking_cards()
    return

while input("Do you want to play a game of Blackjack? type 'y' or 'n': ") == 'y':
    blackjack_full_game()
print("End of the Game.")

