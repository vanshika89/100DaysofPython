import string

alphabet = list(string.ascii_lowercase)


def encrypt_decrypt(user_prefrence, original_text, shift_amount):
    # for letters in original_text:
    pass


game = True
while game:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
    text = input("Type your message:\n").lower()
    shift = input("Type the shift number:\n")
    encrypt_decrypt(direction, text, shift)
    user_message = input("Type 'yes' if you want to go again else type 'no':\n").lower()
    if user_message == 'no':
        print('Goodbye')
        game = False
