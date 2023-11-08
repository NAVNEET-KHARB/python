import random


def code(a):
    words = a.split()
    coded = []
    for word in words:
        if (len(word) >= 3):
            alphr = ["a", "A", "b", "B", "c", "C", "d", "D", "e", "E", "f", "F", "g", "G", "h", "H", "i", "I", "j",
                     "J", "k", "K", "l", "L", "M", "m", "N", "n", "O", "o", "P", "p", "Q", "q", "R", "r", "S", "s", "T", "t", "U", "u", "V", "v", "W", "w", "X", "x", "Y", "y", "Z", "z"]
            salph = ""
            ealph = ""
            pcword = word[1:] + word[0]
            for i in range(0, 3):
                stal = random.randrange(0, len(alphr), 1)
                salph += alphr[stal]
                enal = random.randrange(0, len(alphr), 1)
                ealph += alphr[enal]
            scword = (salph+pcword+ealph)
            coded.append(scword)
        elif (len(word) < 3):
            scword = word[::-1]
            coded.append(scword)
    codedlang = " ".join(coded)
    print(f"The coded language for {a} is\n{codedlang}")


def decode(a):
    words = a.split()
    decoded = []
    for word in words:
        if (len(word) >= 3):
            pdword = word[3:-3]
            ogword = pdword[-1] + pdword[0:-1]
            decoded.append(ogword)
        elif (len(word) < 3):
            ogword = word[::-1]
            decoded.append(ogword)
    decodedlang = " ".join(decoded)
    print(f"The decoded language for\n{a}\nis\n{decodedlang}")


start = input("Do you want to code or decode (C for code or D for decode) : ")
if (start == "C"):
    cde = input("Enter what you want to be coded : ")
    code(cde)
elif (start == "D"):
    dcde = input("Enter the code you want to decode : ")
    decode(dcde)
else:
    print("Enter a valid value.")
