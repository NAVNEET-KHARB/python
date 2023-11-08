import time
# print(time.time())
# time.sleep(3)
# print("After 3 secs")
t = time.localtime()
ft = time.strftime("%Y-%m-%d %H:%M:%S", t)
print(ft)
