import random

rock = '''
    ______
---'   O  )
      (___)
      (___)
      (___)
---.  (___)
'''
paper = '''
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
'''
scissors = '''
    _______
---'   ____)____
          ______)
       (______)
        (____)
---.    (___)
'''
try:
    user_input = int(input("What do you choose? Type 0 for rock, 1 for paper, 2 for scissors.\n"))
    computer_input = random.randint(0, 2)
    input_list = {0: rock, 1: paper, 2: scissors}

    print(input_list[user_input])
    print("Computer choose:", input_list[computer_input])

    if user_input == 0 and computer_input == 2:
        print("You win!")
    if user_input == 2 and computer_input == 0:
        print("You Loose!")
    elif computer_input > user_input:
        print("You Loose!")
    elif computer_input == user_input:
        print("It's a draw!")
    elif computer_input < user_input:
        print("You win!")
except (KeyError, ValueError):
    print("You Typed an invalid number! You loose")
