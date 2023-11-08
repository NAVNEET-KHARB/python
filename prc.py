# f = open("myfile.txt", "r")
# a = f.readlines()
# print(a)
# f = open("ABC.txt", "a")
# f.write("HI")
# f.close()
# f = open("ABC.txt", "r")
# a = f.read()
# print(a)
# with open("ABC.txt", "a") as a:
#     a.write("ab")
# with open("ABC.txt", "r") as b:
#     print(b.read())
# with open("myfile.txt", "r")as w:
#     w.seek(10)
#     print(w.read(5))
# f = open("Himanshu.txt", "x")
# f.close()
# with open("Himanshu.txt", "r") as h:
#     print(h.read())
# def sq(a):
#     return a**2


a = [1, 2, 3, 4]
sqa = list(map(lambda x: x**3, a))
print(sqa)
