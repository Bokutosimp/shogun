print("Welcome to tip calcurator made by Sho!")

bill = int(input("Total bill?: "))
tip = (1 + (int(input("How much tip would you like to give? 10 , 12 , 15 : ")) / 100))
split = int(input("How many people?: "))
each = bill * tip / split

print(f"Each person pay {each:.2f}")