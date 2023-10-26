from sourse import alphabet
from sourse import logo
import os

def ceasar(start_text, shift_amount, cipher_direction):
    end_text = ""
    if cipher_direction == "decode":
        shift_amount *= -1
    for charator in start_text:
        if charator in alphabet:
            position = alphabet.index(charator)
            new_position = position + shift_amount
            end_text += alphabet[new_position]
        else:
            end_text += charator
    print(f"here the {cipher_direction}d result: {end_text}")

run = True
while run:
    os.system('cls')
    print(logo)
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
    text = input("Type your message:\n").lower()
    shift = int(input("Shift amount:"))
    shift = shift % 26
    ceasar(start_text=text, shift_amount=shift, cipher_direction=direction)
    on = input("Type 'yes' to make again\nOtherwise type 'no'")
    if on == "no":
        run = False
        print("Goodbye")

