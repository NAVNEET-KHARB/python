import random


def code(a):
    if (len(a) < 3):
        b = (a[::-1]).lower()
        print(f"The code language for {a} is {b}")
    elif (len(a) > 3):
        b = a.lower()
        aj = b[0]
        na = b.replace(aj, "", 1)
        na += aj
        alphr = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l",
                 "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
        salph = ""
        ealph = ""
        for i in range(0, 3):
            stal = random.randint(0, 51)
            salph += alphr[stal]
            enal = random.randint(0, 51)
            ealph += alphr[enal]
        codedalphs = (salph+na+ealph).replace(" ", "")
        print(f"The code language for {a} is {codedalphs}")


def decode(a):
    if (len(a) < 3):
        b = a[::-1]
        print(f"The decode for {a} is {b}")
    elif (len(a) > 3):
        sa = a[3:-3]
        b = sa[-1]
        na = sa.replace(b, "", 1)
        na = b+na
        print(f"The decode for {a} is {na}")


start = input("Do you want to code or decode (C for code or D for decode) : ")
if (start == "C"):
    cde = input("Enter what you want to be coded : ")
    code(cde)
elif (start == "D"):
    dcde = input("Enter the code you want to decode : ")
    decode(dcde)
else:
    print("Enter a valid value.")
