letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

import random

print("Welcome to password gen made by Sarat!")
n_letter = int(input("How many letters : "))
n_symbol = int(input("How many symbols : "))
n_number = int(input("How many numbers : "))

password = []

for i in range(n_letter):
    password += random.choice(letters)
for j in range(n_symbol):
    password += random.choice(symbols)
for k in range(n_number):
    password += random.choice(numbers)
random.shuffle(password)
real_password = ""
for i in password:
    real_password += i
print(real_password)