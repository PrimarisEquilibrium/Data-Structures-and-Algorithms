def swap(array, a, b):
    array[a], array[b] = array[b], array[a]
    return array

def bubble_sort(array):
    count = 0
    while count <= len(array):
        for i in range(len(array) - 1):
            cur = array[i]
            next = array[i + 1]

            if cur > next:
                array = swap(array, i, i + 1)
    return array


print(bubble_sort([5, 6, 1, 2, 9, 1, 48, 184, 4]))