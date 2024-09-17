def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    def merge(left, right):
        sorted_arr = []
        i = j = 0
        
        while i < len(left) and j < len(right):
            if left[i] <= right[j]:
                sorted_arr.append(left[i])
                i += 1
            else:
                sorted_arr.append(right[j])
                j += 1
        
        while i < len(left):
            sorted_arr.append(left[i])
            i += 1
        while j < len(right):
            sorted_arr.append(right[j])
            j += 1
        
        return sorted_arr

    mid = len(arr) // 2
    left_half = merge_sort(arr[:mid])
    right_half = merge_sort(arr[mid:])
    
    return merge(left_half, right_half)

test_cases = [
    ([31, 23, 35, 27, 11, 21, 15, 28], "Test Case 1"),
    ([22, 34, 25, 36, 43, 67, 52, 13, 65, 17], "Test Case 2")
]

for arr, label in test_cases:
    sorted_arr = merge_sort(arr)
    print(f"{label}: {', '.join(map(str, sorted_arr))}")
