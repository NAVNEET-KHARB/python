import os
pngfiles = []
for files in os.listdir():
    if (files.endswith(".png")):
        pngfiles.append(files)
# print(pngfiles)
i = 1
for file in pngfiles:
    os.rename(f"{file}", f"{i}.png")
    i += 1
