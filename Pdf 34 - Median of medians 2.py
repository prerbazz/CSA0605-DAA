# Function to partition the array around a pivot
def partition(arr, low, high, pivot_index):
    pivot_value = arr[pivot_index]
    # Move pivot to the end
    arr[pivot_index], arr[high] = arr[high], arr[pivot_index]
    store_index = low
    for i in range(low, high):
        if arr[i] < pivot_value:
            arr[store_index], arr[i] = arr[i], arr[store_index]
            store_index += 1
    # Move pivot to its final place
    arr[store_index], arr[high] = arr[high], arr[store_index]
    return store_index

# Function to select a pivot using the median of medians method
def select_pivot(arr, low, high):
    if high - low + 1 <= 5:
        # Sort the subarray and return the median
        return sorted(arr[low:high + 1])[(high - low) // 2]
    
    # Otherwise, divide the array into groups of 5 and find the medians
    medians = []
    for i in range(low, high + 1, 5):
        sublist = sorted(arr[i:min(i + 5, high + 1)])
        medians.append(sublist[len(sublist) // 2])
    
    # Recursively find the median of the medians
    return select_pivot(medians, 0, len(medians) - 1)

# Function to find the k-th smallest element using median of medians algorithm
def median_of_medians(arr, k):
    def kth_smallest(arr, low, high, k):
        if low == high:
            return arr[low]
        
        # Get a pivot using the median of medians
        pivot_index = select_pivot(arr, low, high)
        pivot_index = partition(arr, low, high, pivot_index)
        
        # Rank of the pivot
        rank = pivot_index - low + 1
        
        if rank == k:
            return arr[pivot_index]
        elif k < rank:
            return kth_smallest(arr, low, pivot_index - 1, k)
        else:
            return kth_smallest(arr, pivot_index + 1, high, k - rank)
    
    return kth_smallest(arr, 0, len(arr) - 1, k)

# Example usage:
arr1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
k1 = 6
print("k-th smallest element is:", median_of_medians(arr1, k1))  # Expected Output: 6

arr2 = [23, 17, 31, 44, 55, 21, 20, 18, 19, 27]
k2 = 5
print("k-th smallest element is:", median_of_medians(arr2, k2))  # Expected Output: 21
