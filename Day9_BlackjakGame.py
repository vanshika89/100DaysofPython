import random

cards_dict = {'2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, '10': 10, '11': 11, 'A': 10, 'K': 10,
              'Q': 10, 'J': 10}

user_input = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ")


def deal_card():
    """Returns two random cards from the deck"""
    return random.choices(list(cards_dict.keys()), k=2)


def calculate_score(cards: list):
    """Take a list of cards and return the score calculated from the cards"""
    score = 0
    for key in cards:
        score += cards_dict[key]
    if score == 21 and len(cards) == 2:
        return 0
    elif '11' in cards and score > 21:
        cards.remove('11')
        cards.append('1')
        score = score - 10
    return score


# def play_game()


if user_input == 'y':

    user_cards = deal_card()
    computer_cards = deal_card()

    user_score = calculate_score(user_cards)
    computer_score = calculate_score(computer_cards)

    print(f'Your cards: {user_cards}, current score: {user_score}')
    print(f"Computer's first card: {computer_cards[0]}")

    if 'A' and '10' in user_cards:
        print("You hit Black Jack.You Won!")
        user_input = 'n'
    elif 'A' and '10' in computer_cards:
        print("Computer hit Black Jack.You loose!")
        user_input = 'n'

    user_preference = input("Type 'y' to take another card type 'n' to pass: ")
    if user_preference == 'y':
        user_cards.append(random.choice(list(cards_dict.keys())))
        user_score = calculate_score(user_cards)
        print(f'Your cards: {user_cards}, current score: {user_score}')
        print(f"Computer's first card: {computer_cards[0]}")
        computer_cards.append(random.choice(list(cards_dict.keys())))
        computer_score = calculate_score(computer_cards)
        print(f"Computer's final hand: {computer_cards}, final score: {computer_score}")
    elif user_preference == 'n':
        if 21 < user_score:
            print("You loose!")
        if user_score < 21 < computer_score:
            print("You won!")
        if user_score < 21 and computer_score < 21:
            print("You won!")
        if computer_score < user_score < 21:
            print("You won!")
        if user_score < computer_score < 21:
            print("Computer won won!")
        if user_score == computer_score:
            print("its a Draw!")
