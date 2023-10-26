print("You are lost in mistery forest!")
if input("You came across the path way what you want to go 'left' or 'right' : ").lower() == "right":
    print("Good choice!")
    if input("You see the lake what will you do 'wait' for the boat or 'swim' : ").lower() == "wait":
        print("Your patient pay the prize you got a boat!")
        if input("You see the door in the middle of the lake.\nwhat will you choose 'red' 'blue' 'green' : ").lower() == "green":
            print("Congrat you found the portal to escape!")
        else:
            print("Die")
    else:
        print("Die")
else:
    print("die")