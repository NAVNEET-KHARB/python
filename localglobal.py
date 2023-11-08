# x = 4


# def change():
#     x = 10
#     print(f"Local variable x is {x}")


# change()
# print(f"Global variable x is {x}")
x = 4


def change():
    global x
    x = 10


print(f"Global x is {x}")
change()
print(f"Global x is {x}")
