def max_subarray_sum(nums):
    # Edge case: if nums is empty
    if not nums:
        return 0
    
    # Initialize variables
    current_sum = nums[0]
    max_sum = nums[0]
    
    # Iterate through the array starting from the second element
    for num in nums[1:]:
        # Update current_sum to either the current element or current_sum + current element
        current_sum = max(num, current_sum + num)
        # Update max_sum if current_sum is greater
        max_sum = max(max_sum, current_sum)
    
    return max_sum

# Example usage
nums = [-2,1,-3,4,-1,2,1,-5,4]
print("The maximum subarray sum is:", max_subarray_sum(nums))
