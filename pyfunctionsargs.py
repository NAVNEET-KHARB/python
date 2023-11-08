# def name(fname, mname="Jhon", lname="Whatson"):
#     print("Hello", fname, mname, lname)


# name("Amy")
# name(mname="Kharb", lname="Jaat", fname="Navneet")


# def avg(a, b):
#     avg = (a+b)/2
#     print(avg)


# avg(5, 3)
def avg(*no):
    avgs = 0
    for i in no:
        avgs += i
    return avgs/len(no)


c = avg(3, 4, 6, 1, 99, 33, 223)
print(c)


def name(**names):
    print("Hello", names["fname"], names["mname"], names["lname"])


name(fname="Seth", mname="Freakin", lname="Rollins")
# name(fname="Jhon", lname="Cena")#will produce an error
