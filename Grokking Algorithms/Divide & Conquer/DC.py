# Examples

# 1. Find base cases (simpliest case)
# Tip: For arrays the base case is most likely an empty/contains only one element array 
# 2. Divide to approach the base case

def recursive_sum(arr):
    if arr == []:
        return 0
    return arr[0] + sum(arr) 

def recursive_count(arr):
    if arr == []:
        return 0
    return 1 + recursive_count(arr[1:])

def find_maximum_recursive(arr):
    if len(arr) == 2:
        return arr[0] if arr[0] > arr[1] else arr[1]
    sub_max = find_maximum_recursive(arr[1:])
    return arr[0] if arr[0] > sub_max else sub_max