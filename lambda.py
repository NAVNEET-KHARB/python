# double = lambda x:x*2
# print(double(5))
# sum2 = lambda x,y:x+y
# print(sum2(2,3))
def apl(fx, val):
    return val+fx(val)


print(apl(lambda x: x**3, 7))
