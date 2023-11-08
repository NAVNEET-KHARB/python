n = int(input())
i = 0
s = set()
while (i < n):
    it = int(input())
    s.add(it)
    i += 1
le = 0
sle = 0
t = tuple(s)
for j in t:
    print(j, "a")
    if (j > le):
        le, sle = j, le
print(sle)
