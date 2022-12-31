def mergesort(array):
    if len(array) > 1:
        mid = len(array) // 2
        left = array[:mid]
        right = array[mid:]

        # recursion to split array
        mergesort(left)
        mergesort(right)

        l = 0 # left array index
        r = 0 # right array index
        k = 0 # merged array index

        # While loop comparing each left most value to right while updating pointers
        while l < len(left) and r < len(right):
            if left[l] <= right[r]:
                array[k] = left[l]
                l += 1
            else:
                array[k] = right[r]
                r += 1
            k += 1
        
        # Transferring left/right array to the merged array in the case that one or the other is empty
        while l < len(left):
            array[k] = left[l]
            l += 1
            k += 1
        
        while r < len(right):
            array[k] = right[r]
            r += 1
            k += 1

        return array

print(mergesort([5, 1, 4, 9, 10, 11, 3, 6]))