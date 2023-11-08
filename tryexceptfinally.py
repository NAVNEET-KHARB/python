# try:
#     l = [1, 2, 3, 4]
#     i = int(input("Enter an index : "))
#     print(l[i])
# except:
#     print("Some error occured.")
# finally:
#     print("Thanks")
# def func1():
#     try:
#         l = [1, 2, 3, 4]
#         i = int(input("Enter an index : "))
#         print(l[i])
#         return 1
#     except:
#         print("Some error occured.")
#         return 0
#     print("Thanks")


# x = func1()
# print(x)


def func1():
    try:
        l = [1, 2, 3, 4]
        i = int(input("Enter an index : "))
        print(l[i])
        return 1
    except:
        print("Some error occured.")
        return 0
    finally:
        print("Thanks")


x = func1()
print(x)
