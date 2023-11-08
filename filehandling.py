# f = open("myfile.txt", "r")
# f = open("myfile.txt", "x")
# print(f)
# f = open("myfile.txt", "r")
# text = f.read()
# print(text)
# f = open("myfile.txt", "w")
# f.write("Hi, I am written using filehandling")
# f.close()
with open("myfile.txt", "a") as f:
    f.write(" I am appended.")

with open("myfile.txt", "r") as f:
    text = f.read()
    print(text)
