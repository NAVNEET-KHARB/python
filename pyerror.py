# salary = int(input("Enter your salary : "))
# if (not 2000 < salary < 5000):
#     raise ValueError("Not a valid salary")
a = input("Enter a no. between 5 and 9 : ")
if (a == "quit"):
    print("Thanks for your time.")
elif (int(a) < 5 or int(a) > 9):
    raise ValueError("The no. should be between 5 and 9")
elif (5 <= int(a) <= 9):
    print(a)
elif (a != "quit"):
    raise ValueError("The no. should be between 5 and 9")
