# a = int(input("Enter your age : "))
# print("Your age is :", a)
# if (a >= 18):
#     print("You can drive")
# else:
#     print("You cannot drive")
num = int(input("Enter a number : "))
# if (num < 0):
#     print("Entered number :", num, "is negative")
# elif (num == 0):
#     print("Entered number :", num, "is zero")
# else:
#     print("Entered number :", num, "is positive")
if (num < 0):
    print("Entered number :", num, "is negative")
elif (num == 0):
    print("Entered number :", num, "is zero")
else:
    if (num > 0 and num <= 10):
        print("Entered number :", num)
    elif (num > 10 and num <= 20):
        print("Entered number :", num)
    else:
        print("Entered number :", num, "is greater than 20")
