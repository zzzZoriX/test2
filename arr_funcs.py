def filter_greater(arr, value):
    new_arr = []
    for el in arr:
        if(el > value): new_arr.append(el)

    return new_arr

def filter_less(arr, value):
    new_arr = []
    for el in arr:
        if(el < value): new_arr.append(el)

    return new_arr

def filter_equal(arr, value):
    new_arr = []
    for el in arr:
        if(el == value): new_arr.append(el)

    return new_arr

def filter_not_equal(arr, value):
    new_arr = []
    for el in arr:
        if(el != value): new_arr.append(el)

    return new_arr

def test():
    test_arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]

    print(filter_greater(test_arr, 5))
    print(filter_less(test_arr, 5))
    print(filter_equal(test_arr, 5))
    print(filter_not_equal(test_arr, 5))