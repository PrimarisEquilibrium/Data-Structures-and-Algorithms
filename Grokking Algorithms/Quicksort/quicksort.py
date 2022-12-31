def quicksort(array):
    if len(array) < 2:
        return array # Base Case: arrays with 0 or 1 element are already "sorted"
    else:
        pivot = array[0] # Recursive Case
        less = [i for i in array[1:] if i <= pivot] # Subarray of all the elements less than the pivot

        greater = [i for i in array[1:] if i >= pivot] # Subarray of all the elements greater than the pivot

        return quicksort(less) + [pivot] + quicksort(greater)