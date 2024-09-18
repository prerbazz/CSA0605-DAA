def meet_in_the_middle(arr, target):
    # Helper function to get all subset sums
    def get_subset_sums(subset):
        n = len(subset)
        sums = []
        # Generate all subset sums
        for i in range(1 << n):  # 2^n subsets
            current_sum = 0
            for j in range(n):
                if i & (1 << j):  # Check if j-th element is in the subset
                    current_sum += subset[j]
            sums.append(current_sum)
        return sums

    # Split the array into two halves
    mid = len(arr) // 2
    left_half = arr[:mid]
    right_half = arr[mid:]

    # Get all subset sums of both halves
    left_sums = get_subset_sums(left_half)
    right_sums = get_subset_sums(right_half)

    # Sort the sums of the right half
    right_sums.sort()

    # Check if there's a subset sum exactly equal to target
    for left_sum in left_sums:
        remaining = target - left_sum

        # Binary search for remaining sum in right_sums
        low, high = 0, len(right_sums) - 1
        while low <= high:
            mid = (low + high) // 2
            if right_sums[mid] == remaining:
                return True  # Exact sum found
            elif right_sums[mid] < remaining:
                low = mid + 1
            else:
                high = mid - 1

    return False  # No exact sum found

# Example usage
arr1 = [1, 3, 9, 2, 7, 12]
target1 = 15
print("Subset with exact sum 15:", meet_in_the_middle(arr1, target1))  # Output: True

arr2 = [3, 34, 4, 12, 5, 2]
target2 = 15
print("Subset with exact sum 15:", meet_in_the_middle(arr2, target2))  # Output: True
