import time
timestamp = time.strftime("%H")
# timestamp = input("Enter hour")
ts1 = int(timestamp)
if (ts1 >= 5 and ts1 < 12):
    print("Good Morning!!!")
elif (ts1 >= 12 and ts1 < 16):
    print("Good Afternoon!!!")
elif (ts1 >= 16 and ts1 < 21):
    print("Good Evening!!!")
else:
    print("Good Night!!!")
