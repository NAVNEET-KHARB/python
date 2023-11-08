no = int(input("Enter a no."))
match no:
    case _ if no < 0:
        print("Negative number")
    case _ if no == 0:
        print("Neither odd nor even")
    case _ if no % 2 == 0:
        print("Even number")
    case _ if no % 2 != 0:
        print("Odd number")
    case _:
        print("Enter a valid number")
