import string

alphabet = list(string.ascii_lowercase)


def encrypt_decrypt(user_prefrence, original_text, shift_amount):
    cipher_text = ''
    for letter in original_text:
        if ' ' in letter:
            cipher_text += ' '
        if user_prefrence == 'decode':
            shift_amount *= -1

        new_location = alphabet.index(letter) + shift_amount
        new_location %= len(alphabet)
        cipher_text += alphabet[new_location]
    print(f"Here is the {user_prefrence} result: {cipher_text}")


direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))
if direction == 'encode' or 'decode':
    encrypt_decrypt(direction, text, shift)
else:
    print('Choose from the given option')

# user_message = input("Type 'yes' if you want to go again else type 'no':\n").lower()
# if user_message == 'no':
#     print('Goodbye')
#     game = False
