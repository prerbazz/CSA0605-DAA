def median_of_medians(arr, k):
    
    def partition(arr, pivot):
        less = [x for x in arr if x < pivot]
        equal = [x for x in arr if x == pivot]
        greater = [x for x in arr if x > pivot]
        return less, equal, greater

    def select(arr, k):
        if len(arr) <= 5:
            return sorted(arr)[k]

        # Step 1: Divide arr into groups of 5
        groups = [arr[i:i + 5] for i in range(0, len(arr), 5)]
        
        # Step 2: Find the median of each group
        medians = [sorted(group)[len(group) // 2] for group in groups]
        
        # Step 3: Find the median of medians
        median_of_medians = select(medians, len(medians) // 2)
        
        # Step 4: Partition the array
        less, equal, greater = partition(arr, median_of_medians)
        
        # Step 5: Determine which subarray to recurse into
        if k < len(less):
            return select(less, k)
        elif k < len(less) + len(equal):
            return median_of_medians
        else:
            return select(greater, k - len(less) - len(equal))
    
    return select(arr, k)

arr = [12, 3, 5, 7, 4, 19, 26]
k = 4  # Find the 4th smallest element (0-based index)
result = median_of_medians(arr, k)
print(f"The {k+1}-th smallest element is {result}")
