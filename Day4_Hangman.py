import random

word_list = ['success', 'building']

chosen_word = random.choice(word_list)
print(chosen_word)

word_dash = ''
for _ in chosen_word:
    word_dash += '_'
print("Word to guess: ", word_dash)

length = len(chosen_word)
game_over = False
# life = 6
correct_letters = []
while not game_over:
    display = ''
    guessed_letter = input("Guess a letter: ").lower()
    for letter in chosen_word:
        if guessed_letter == letter:
            display+=guessed_letter
            correct_letters.append(guessed_letter)
        elif letter in correct_letters:
            correct_letters.append(guessed_letter)
        else:
            # life -= 1
            display.append('_')
    print('Word to guess', ''.join(display))
    # if life <= 0 or '_' not in display:
    if '_' not in display:
        game_over = True
