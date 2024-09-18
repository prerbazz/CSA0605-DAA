def climbStairs(n):
    # Base cases for 1 or 2 steps
    if n == 1:
        return 1
    if n == 2:
        return 2
    
    # Variables to store the number of ways to reach the last two steps
    prev1 = 2  # ways to reach step 2
    prev2 = 1  # ways to reach step 1
    
    # Iterate through steps 3 to n and calculate the number of ways
    for i in range(3, n+1):
        current = prev1 + prev2
        prev2 = prev1
        prev1 = current
    
    return prev1

# Example Usage:
print("Number of ways to climb 4 steps:", climbStairs(4))  # Output: 5
print("Number of ways to climb 3 steps:", climbStairs(3))  # Output: 3
