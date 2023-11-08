lst1 = ["red", "Green", "Yellow", "Blue", "Green"]
# print(lst1)
# print(type(lst1))
# print(lst1[0])
# print(lst1[1])
# print(lst1[2])
# print(lst1[3])
# print(lst1[-1])
# print(lst1[-2])
# print(lst1[-3])
# # print(lst1[-4])
# if 'Yellow' in lst1:
#     print("Yellow is present.")
# else:
#     print("Yellow is absent.")
# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10,
#            11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
# print(numbers[5:18:2])
# print(numbers[5:18])
# print(numbers[1:20:2])
# names = ["Milo", "Sarah", "Bruno", "Anastasia", "Rose"]
# nameWith_o = [item for item in names if "o" in item]
# print(nameWith_o)
jmp = 1
starting = 0
starting = int(input("Enter the no, where you want your sqrts from : "))
no = int(input("Enter the no till you want your sqrt : "))
stepcnfrm = input(
    "Do you want to print sqrt for certain patterns?\nPlease answer in \"Y or N\" : ")
if (stepcnfrm == "Y"):
    jmp = int(input("Enter the no. you want to have your sqrts a gap of : "))
elif (stepcnfrm == "N"):
    jmp = 1
else:
    print("Enter a valid response.")
sqrt = [i*i for i in range(starting, no+1, jmp)]
print(sqrt)
