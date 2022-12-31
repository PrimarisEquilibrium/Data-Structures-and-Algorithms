"""Implement quick sort in Python.
Input a list.
Output a sorted list."""

def quicksort(arr, left, right):
    if left < right: # Subarray contains atleast 2 elements

        # Performs a partition on the array, then outputs the position of the pivot after the process
        partition_pos = partition(arr, left, right)

        # Calls quicksort on elements smaller than pivot
        quicksort(arr, left, partition_pos - 1)

        # Calls quicksort on elements larger than pivot
        quicksort(arr, partition_pos + 1, right)
    
    return arr

def partition(arr, left, right):

    # i moves to the right
    # looks for values smaller than pivot
    i = left

    # j moves to the left
    # looks for values larger than pivot
    j = right - 1

    pivot = arr[right]

    # i and j move like this they cross
    while i < j:

        # While in bounds and value is smaller than pivot
        while i < right and arr[i] < pivot:
            i += 1
        
        # While in bounds and value is larger than pivot
        while j > left and arr[j] >= pivot:
            j -= 1

        # Check if elements have crossed yet and if they haven't
        if i < j:

            # Swap the element positions at index i with index j
            arr[i], arr[j] = arr[j], arr[i]
    
    # If the while looks breaks meaning i and j have crossed ...
    if arr[i] > pivot:

        # ... swap i with the pivot point (right most element in array)
        arr[i], arr[right] = arr[right], arr[i]
    
    # Returns the pivot point
    # Needed to split the array to perform quicksort in both arrays
    # After i is swapped with pivot, i is the position where the pivot points lies
    return i
    
array = [21, 4, 1, 3, 9, 20, 25, 6, 21, 14]
print(quicksort(array, 0, len(array) - 1))