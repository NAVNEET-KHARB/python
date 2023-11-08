import os
if (not os.path.exists("data")):
    os.mkdir("data")
# for i in range(0,100):
    # os.mkdir(f"data/day{i+1}")
    # os.rename(f"data/day{i+1}",f"data/Day {i+1}")
folders = os.listdir("data")
# print(folders)
# print(os.getcwd())
# os.chdir("/Users")
# print(os.getcwd())
for folder in folders:
    print(folder)
    print(os.listdir(f"data/{folder}"))