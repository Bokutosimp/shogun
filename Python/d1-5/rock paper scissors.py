rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''


import random

def check(you, bot):
    if you == bot:
        print("Draw!")
    elif you == 0 and bot == 2:
        print("You win!")
    elif you > bot:
        print("You win!")
    else:
        print("You lost")


choice = [rock, paper, scissors]
you = int(input("What you chose?\n'1' for rock , '2' for paper , '3' for scissors: ")) - 1
bot = random.randint(0, 2)

if you > 2 or you < 0:
    print("Invalid choice")
else:
    player = choice[you]
    com = choice[bot]
    print(f"You chose :\n{player}")
    print(f"Bot chose :\n{com}")
    check(you, bot)