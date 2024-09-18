def rob(nums):
    # Helper function to calculate the max money for a linear sequence of houses
    def rob_linear(houses):
        n = len(houses)
        if n == 0:
            return 0
        if n == 1:
            return houses[0]
        if n == 2:
            return max(houses[0], houses[1])
        
        # DP array to store the max money that can be robbed up to house i
        dp = [0] * n
        dp[0] = houses[0]
        dp[1] = max(houses[0], houses[1])
        
        for i in range(2, n):
            dp[i] = max(dp[i-1], dp[i-2] + houses[i])
        
        return dp[-1]
    
    # Edge case: If there's only one house, return the value of that house
    if len(nums) == 1:
        return nums[0]
    
    # Rob houses from 0 to n-2 (excluding the last house)
    money1 = rob_linear(nums[:-1])
    # Rob houses from 1 to n-1 (excluding the first house)
    money2 = rob_linear(nums[1:])
    
    # Take the maximum of the two robbery plans
    return max(money1, money2)

# Example usage:
nums1 = [2, 3, 2]
print("Maximum money to rob:", rob(nums1))  # Output: 3

nums2 = [1, 2, 3, 1]
print("Maximum money to rob:", rob(nums2))  # Output: 4
  
