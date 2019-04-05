arr = [2, 5, 8, 12, 16, 23, 38, 56, 72, 91]


def binary_search(array, number):
    new_array = array
    value = None
    n = 0

    while number != value:
        splitter = round(len(new_array) / 2)
        right_array = new_array[splitter:]
        left_array = new_array[0:splitter]
        if right_array[0] == number:
            value = number
            n += 1
        elif right_array[0] < number:
            new_array = right_array
            n += 1
        else:
            new_array = left_array
            n += 1
    return n


print(binary_search(arr, 2))


# Recursion
def binary_search_recursion(array, l, r, x):
    if r >= l:
        mid = l + (r - l) / 2
        if array[mid] == x:
            return mid
        elif array[mid] > x:
            return binary_search_recursion(array, l, mid - 1, x)
        else:
            return binary_search_recursion(array, mid + 1, r, x)
    else:
        return -1
