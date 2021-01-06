def bubble(list_a):
    index = len(list_a) - 1
    sorted = False

    while not sorted:
        sorted = True
        i: int
        for i in range(index):
            if list_a[i] > list_a[i + 1]:
                sorted = False
                list_a[i], list_a[i + 1] = list_a[i + 1], list_a[i]
    return list_a


print(bubble([5,6,4,9,8,2,4,1,5,7,3]))


