MOD = 10**9 + 7

# Function to calculate the maximum sum of subsequence with no adjacent elements
def max_non_adjacent_sum(nums):
    n = len(nums)
    if n == 0:
        return 0
    if n == 1:
        return nums[0]
    
    prev1, prev2 = 0, 0
    
    for num in nums:
        curr = max(num + prev2, prev1)
        prev2 = prev1
        prev1 = curr
    
    return curr % MOD

def solve(nums, queries):
    total_sum = 0
    
    for posi, xi in queries:
        nums[posi] = xi
        max_sum = max_non_adjacent_sum(nums)
        total_sum = (total_sum + max_sum) % MOD
    
    return total_sum

# Input format
n, q = map(int, input().split())
nums = list(map(int, input().split()))
queries = [tuple(map(int, input().split())) for _ in range(q)]

# Output the result
print(solve(nums, queries))
  
