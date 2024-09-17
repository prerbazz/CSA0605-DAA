def find_min_max(arr):
    if not arr:
        raise ValueError("Array is empty")
    
    min_value = arr[0]
    max_value = arr[-1]
    
    return min_value, max_value

test_cases = [
    ([2, 4, 6, 8, 10, 12, 14, 18], "Test Case 1"),
    ([11, 13, 15, 17, 19, 21, 23, 35, 37], "Test Case 2"),
    ([22, 34, 35, 36, 43, 67, 12, 13, 15, 17], "Test Case 3")
]

for arr, label in test_cases:
    min_val, max_val = find_min_max(arr)
    print(f"{label}: Min = {min_val}, Max = {max_val}")
