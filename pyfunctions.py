def calculateGmean(a, b):
    mean = (a*b)/(a+b)
    print(mean)


a = 9
b = 6
c = 4
d = 1
calculateGmean(a, b)
calculateGmean(c, d)


def swap(fno, sno):
    tempno = fno
    fno = sno
    sno = tempno
    print("Numbers are swapped\nNow,first no. is :",
          fno, "\nSecond no. is :", sno)


swap(a, b)
swap(c, d)
