# n = input("Enter a number : ")
# print(f"The multiplication table of {n} is :")
# for i in range(1, 11):
#     print(f"{n} X {i} = {int(n)*i}")
# print("Some imp lines of code")
# print("EOP")
# n = input("Enter a number : ")
# print(f"The multiplication table of {n} is :")
# try:
#     for i in range(1, 11):
#         print(f"{n} X {i} = {int(n)*i}")
# except:
#     print("Some error occured.")
# print("Some imp lines of code")
# print("EOP")
# n = input("Enter a number : ")
# print(f"The multiplication table of {n} is :")
# try:
#     for i in range(1, 11):
#         print(f"{n} X {i} = {int(n)*i}")
# except Exception as e:
#     print(e)
# print("Some imp lines of code")
# print("EOP")
try:
    num = int(input("Enter a number :"))
    a = [6, 4, 1]
    print(a[num])
except ValueError:
    print("Number enterd isn't an integer.")
except IndexError:
    print("Index Error")
