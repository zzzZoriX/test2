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