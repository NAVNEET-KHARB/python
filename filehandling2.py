# with open("myfile.txt", "r") as f:
# frd = f.readline(2)
# print(frd)
# while True:
#     line = f.readline()
#     if (not line):
#         break
#     print(line)
# with open("marks.txt", "r") as m:
#     i = 1
#     while True:
#         mark = m.readline()
#         if not mark:
#             break
#         m1 = int(mark.split(",")[0])
#         m2 = int(mark.split(",")[1])
#         m3 = int(mark.split(",")[2])
#         avg = (m1+m2+m3)/3
#         pct = ((m1+m2+m3)/150)*100
#         print(f"The marks of student{i} in maths are {m1}")
#         print(f"The marks of student{i} in physics are {m2}")
#         print(f"The marks of student{i} in chemistry are {m3}")
#         print(f"The average marks of student{i} are {avg}")
#         print(f"The percentage of student{i} is {pct}\n")
#         i += 1
with open("myfile2.txt", "w") as w:
    # lines = ["line1\n", "line2\n", "line3\n"]
    # w.writelines(lines)
    lines = ["hey", "hi", "bye"]
    for line in lines:
        w.write(line + "\n")
