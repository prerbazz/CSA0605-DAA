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
print(selection_sort([]))  # Expected Output: []
print(selection_sort([1]))  # Expected Output: [1]
print(selection_sort([7, 7, 7, 7]))  # Expected Output: [7, 7, 7, 7]
print(selection_sort([-5, -1, -3, -2, -4]))  # Expected Output: [-5, -4, -3, -2, -1]
