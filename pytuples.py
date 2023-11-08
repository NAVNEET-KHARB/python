tup = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20)
# print(type(tup), tup)
# t1 = (1)
# print(type(t1), t1)
# t2 = (1,)
# print(type(t2), t2)
print(tup[3])
print(tup[-3])
if 9 in tup:
    print("Yes")
else:
    print("No")
print(tup[0::2])
for i in tup:
    print(i, end="[]")
