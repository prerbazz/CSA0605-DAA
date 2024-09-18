def meet_in_the_middle(arr, target):
    def get_subset_sums(subset):
        n = len(subset)
        sums = []
        
        for i in range(1 << n):  
            current_sum = 0
            for j in range(n):
                if i & (1 << j):  
                    current_sum += subset[j]
            sums.append(current_sum)
        return sums

  
    mid = len(arr) // 2
    left_half = arr[:mid]
    right_half = arr[mid:]

    # Get all subset sums of both halves
    left_sums = get_subset_sums(left_half)
    right_sums = get_subset_sums(right_half)

    # Sort the sums of the right half
    right_sums.sort()

    # Track the closest sum
    closest_sum = float('inf')
    
    # Helper function to find the closest value in sorted right_sums
    def find_closest_sum(target_sum):
        low, high = 0, len(right_sums) - 1
        closest = right_sums[0]
        
        while low <= high:
            mid = (low + high) // 2
            if right_sums[mid] == target_sum:
                return right_sums[mid]
            if abs(right_sums[mid] - target_sum) < abs(closest - target_sum):
                closest = right_sums[mid]
            if right_sums[mid] < target_sum:
                low = mid + 1
            else:
                high = mid - 1
        return closest

    # Find the closest sum by combining left and right subset sums
    for left_sum in left_sums:
        remaining = target - left_sum
        closest_in_right = find_closest_sum(remaining)
        total_sum = left_sum + closest_in_right
        if abs(total_sum - target) < abs(closest_sum - target):
            closest_sum = total_sum

    return closest_sum

# Example usage
a = [45, 34, 4, 12, 5, 2]
target_a = 42
print("Closest sum to", target_a, "is:", meet_in_the_middle(a, target_a))

b = [1, 3, 2, 7, 4, 6]
target_b = 10
print("Closest sum to", target_b, "is:", meet_in_the_middle(b, target_b))
