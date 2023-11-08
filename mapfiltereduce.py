from functools import reduce


def cube(x):
    return (x**3)


def filtered(x):
    return (x % 2 == 0)


l = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# nl = map(cube, l)
# print(nl)
# nl = list(map(cube, l))
# print(nl)
# nnl = filter(filtered, l)
# print(nnl)
# nnl = list(filter(filtered, l))
# print(nnl)
rl = reduce(lambda x, y: x+y, l)
print(rl)
