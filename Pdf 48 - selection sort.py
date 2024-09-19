def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_index = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_index]:
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]
    return arr

# Test cases
print(selection_sort([5, 2, 9, 1, 5, 6]))  # Output: [1, 2, 5, 5, 6, 9]
print(selection_sort([10, 8, 6, 4, 2]))  # Output: [2, 4, 6, 8, 10]
print(selection_sort([1, 2, 3, 4, 5]))  # Output: [1, 2, 3, 4, 5]
