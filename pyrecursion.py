def factorial(n):
    if (n == 0 or n == 1):
        return 1
    else:
        return (n*factorial(n-1))


print(factorial(4))


def fibonacci(n):
    lstfs = [0, 1]
    for i in range(2, n):
        lstfs.append(lstfs[i-1]+lstfs[i-2])
    return lstfs


print(fibonacci(25))
