def func1(arr):
    sum = 0
    product = 1
    for i in range(0, len(arr)):
        sum += arr[i]

    for i in range(0, len(arr)):
        product *= arr[i]
    print(sum, product)


a = [3, 4, 5, 3]
func1(a)
