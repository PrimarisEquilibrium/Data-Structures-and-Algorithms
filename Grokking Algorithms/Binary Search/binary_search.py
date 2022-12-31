def binary_search(array, item):
    low = 0
    high = len(array) - 1

    while low <= high: # While the search area hasn't been narrowed down to one element
        mid = (low + high) // 2
        guess = array[mid]
        if guess == item: # Guess is correct
            return mid
        if guess > item: # Guess is larger than item, reducing the search area to the first half
            high = mid - 1
        else: # Guess is smaller than item, reducing the search area to the second half
            low = mid + 1
    return None

my_list = [1, 3, 5, 7, 9]

print(binary_search(my_list, 3))
print(binary_search(my_list, -1))