def partition(arr, low, high, pivot):
    pivot_val = arr[pivot]
    # Move pivot element to end
    arr[pivot], arr[high] = arr[high], arr[pivot]
    i = low
    for j in range(low, high):
        if arr[j] < pivot_val:
            arr[i], arr[j] = arr[j], arr[i]
            i += 1
    # Swap back the pivot to its final place
    arr[i], arr[high] = arr[high], arr[i]
    return i

def select_pivot(arr, low, high):
    # If there are less than or equal to 5 elements, sort them and return the median
    if high - low <= 5:
        sublist = sorted(arr[low:high + 1])
        return low + len(sublist) // 2
    
    # Otherwise, divide the array into groups of 5 and find the medians
    medians = []
    for i in range(low, high + 1, 5):
        group = sorted(arr[i:min(i + 5, high + 1)])
        medians.append(group[len(group) // 2])
    
    # Recursively find the median of medians
    return select_pivot(medians, 0, len(medians) - 1)

def kth_smallest(arr, low, high, k):
    if low == high:
        return arr[low]

    # Get a pivot using the median of medians
    pivot_index = select_pivot(arr, low, high)
    
    # Partition the array around the pivot and get its final position
    pivot_position = partition(arr, low, high, pivot_index)
    
    # Calculate the rank of the pivot
    rank = pivot_position - low + 1
    
    if rank == k:
        return arr[pivot_position]
    elif k < rank:
        return kth_smallest(arr, low, pivot_position - 1, k)
    else:
        return kth_smallest(arr, pivot_position + 1, high, k - rank)

# Helper function to call kth_smallest
def find_kth_smallest(arr, k):
    return kth_smallest(arr, 0, len(arr) - 1, k)

# Example usage
arr1 = [12, 3, 5, 7, 19]
k1 = 2
print("k-th smallest element is", find_kth_smallest(arr1, k1))  # Expected Output: 5

arr2 = [12, 3, 5, 7, 4, 19, 26]
k2 = 3
print("k-th smallest element is", find_kth_smallest(arr2, k2))  # Expected Output: 5

arr3 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
k3 = 6
print("k-th smallest element is", find_kth_smallest(arr3, k3))  # Expected Output: 6
      
