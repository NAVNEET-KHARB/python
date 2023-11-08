import random
ch = int(input("Do we start the game? (1 for start,0 for abort) : "))
while (ch == 1):
    user = int(
        input("Enter what you choose\n0 for snake\n1 for water\n2 for gun\n"))
    if (user == 0):
        u = "snake"
    elif (user == 1):
        u = "water"
    elif (user == 2):
        u = "gun"
    else:
        print("Enter a legal choice!")
        break
    comp = random.randrange(0, 3, 1)
    if (comp == 0):
        c = "snake"
    elif (comp == 1):
        c = "water"
    else:
        c = "gun"
    if (user == comp):
        print(f"Welp!, it's a tie! You chose {u} while computer chose {c}")
    elif (user == 0 and comp == 1):
        print(f"Yay, you won! You chose {u} while computer chose {c}")
    elif (user == 1 and comp == 2):
        print(f"Yay, you won! You chose {u} while computer chose {c}")
    elif (user == 2 and comp == 0):
        print(f"Yay, you won! You chose {u} while computer chose {c}")
    else:
        print(f"Alas, you lost! You chose {u} while computer chose {c}")
    ch = int(input("Do you want to play more? (1 for continue,0 for exit) : "))
