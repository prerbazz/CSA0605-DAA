def kadane(nums):
    max_sum = float('-inf')
    current_sum = 0
    for num in nums:
        current_sum = max(num, current_sum + num)
        max_sum = max(max_sum, current_sum)
    return max_sum

def min_kadane(nums):
    min_sum = float('inf')
    current_sum = 0
    for num in nums:
        current_sum = min(num, current_sum + num)
        min_sum = min(min_sum, current_sum)
    return min_sum

def max_circular_subarray_sum(nums):
    max_kadane = kadane(nums)
    total_sum = sum(nums)
    
    # Invert the array to find the minimum subarray sum
    nums = [-num for num in nums]
    min_kadane = min_kadane(nums)
    
    # Calculate the maximum circular subarray sum
    max_circular = total_sum + min_kadane
    
    # If all elements are negative, max_circular will be equal to total_sum
    if max_circular == total_sum:
        return max_kadane
    
    return max(max_kadane, max_circular)

# Example usage
nums = [1, -2, 3, -2]
print("The maximum sum of a circular subarray is:", max_circular_subarray_sum(nums))
