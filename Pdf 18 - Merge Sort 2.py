def merge_sort(arr):
    comparisons[0] = 0 
    def merge(left, right):
        sorted_arr = []
        i = j = 0
        
        while i < len(left) and j < len(right):
            comparisons[0] += 1  
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

    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left_half = merge_sort(arr[:mid])
    right_half = merge_sort(arr[mid:])
    
    return merge(left_half, right_half)

comparisons = [0]

test_cases = [
    ([12, 4, 78, 23, 45, 67, 89, 1], "Test Case 1"),
    ([38, 27, 43, 3, 9, 82, 10], "Test Case 2")
]

for arr, label in test_cases:
    sorted_arr = merge_sort(arr)
    print(f"{label}: {', '.join(map(str, sorted_arr))}")
    print(f"Number of comparisons: {comparisons[0]}")
