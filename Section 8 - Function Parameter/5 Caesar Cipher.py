
alphabet = ['a', 'b', 'c', 'd', 'e', 'f','g', 'h', 'i', 'j', 'k', 'l','m', 'n', 'o', 'p', 'q', 'r','s', 't', 'u', 'v', 'w', 'x', 'y','z',
'a', 'b', 'c', 'd', 'e', 'f','g', 'h', 'i', 'j', 'k', 'l','m', 'n', 'o', 'p', 'q', 'r','s', 't', 'u', 'v', 'w', 'x', 'y','z']

direction = input("Type 'encode' to encrypt , Type 'decode' to decrypt: \n")
text= input("Type your message: \n").lower()
shift = int(input("Type shift number:\n"))


def encrypt(plaintext, shift_amount):
    ciphertext = ""
    for letter in plaintext:
        position = alphabet.index(letter)
        new_position = position + shift_amount
        new_letter = alphabet[new_position]
        ciphertext += new_letter
    print(f"The encoded text is: {ciphertext}")

encrypt(plaintext = text, shift_amount = shift)