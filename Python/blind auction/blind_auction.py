import os
from art import logo

def find_highest(record):
    highest = 0
    winner = ""
    for i in record:
        amount = record[i]
        if amount > highest:
            highest = amount
            winner = i
    print(f"The winner is {winner} with aa bit of ${highest}")
list = {}
run = True
while run:
    print(logo)
    name = input("What is your name?: ")
    bit = int(input("How much you want to bit?: "))
    list[name] = bit
    choice = input("Is there are player left\ntype 'y' if yes , 'n' if no: ")
    if choice == "n":
        run = False
        find_highest(list)
    elif choice == "y":
        os.system('cls')
