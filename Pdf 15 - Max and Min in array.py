def find_min_max(arr):
    if not arr:
        raise ValueError("Array is empty")
    
    min_value = arr[0]
    max_value = arr[0]
    
    for num in arr[1:]:
        if num < min_value:
            min_value = num
        if num > max_value:
            max_value = num
            
    return min_value, max_value

test_cases = [
    ([5, 7, 3, 4, 9, 12, 6, 2], "Test Case 1"),
    ([1, 3, 5, 7, 9, 11, 13, 15, 17], "Test Case 2"),
    ([22, 34, 35, 36, 43, 67, 12, 13, 15, 17], "Test Case 3")
]

for arr, label in test_cases:
    min_val, max_val = find_min_max(arr)
    print(f"{label}: Min = {min_val}, Max = {max_val}")
