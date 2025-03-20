import random

cards_dict = {'2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, '10': 10, 'A': 1, 'K': 10, 'Q': 10,
              'J': 10}

user_input = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ")


def calculate_score(cards: list):
    score = 0
    for key in cards:
        score += cards_dict[key]
    return score


if user_input == 'y':
    user_cards = random.choices(list(cards_dict.keys()), k=2)
    user_score = calculate_score(user_cards)
    print(f'Your cards: {user_cards}, current score: {user_score}')
    computer_cards = random.choices(list(cards_dict.keys()), k=2)
    computer_score = calculate_score(computer_cards)
    print(f"Computer's first card: {computer_cards[0]}")
    user_preference = input("Type 'y' to take another card type 'n' to pass: ")
    if user_preference == 'y':
        user_cards.append(random.choice(list(cards_dict.keys())))
        user_score = calculate_score(user_cards)
        print(f'Your cards: {user_cards}, current score: {user_score}')
        print(f"Computer's first card: {computer_cards[0]}")
    elif user_preference == 'n':
        computer_cards.append(random.choice(list(cards_dict.keys())))
        computer_score = calculate_score(computer_cards)
        print(f"Computer's final hand: {computer_cards}, final score: {computer_score}")
