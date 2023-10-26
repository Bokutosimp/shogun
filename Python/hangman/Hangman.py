import hart
import hword
import random
import os

word = random.choice(hword.word_list)
wordl = len(word)
live = 6
run = True


os.system('cls')
print(hart.logo)

display = []

for _ in range(wordl):
    display += "_"

while run:
    guess = input("What do you guess? : ").lower()

    os.system('cls')

    if guess in display:
        print(f"you already guess {guess}")

    for i in range(wordl):
        letter = word[i]
        if letter == guess:
            display[i] = letter
    
    if guess not in word:
        print(f"You guess {guess}, that not in word. you lose your life!")
        live -= 1
        if live == 0:
            print("You Die!")
            print(f"the word is {word}")
            run = False

    if "_" not in display:
        run = False
        print("You Win")

    print(f"{' '.join(display)}")

    print(hart.stages[live])
        


