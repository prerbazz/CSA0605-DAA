def fourSumCount(A, B, C, D):
    # Dictionary to store sums of pairs from A and B
    sum_map = {}
    
    # Calculate all sums of pairs from A and B and store them in the hash map
    for a in A:
        for b in B:
            sum_ab = a + b
            if sum_ab in sum_map:
                sum_map[sum_ab] += 1
            else:
                sum_map[sum_ab] = 1
    
    count = 0
    
    # Calculate all sums of pairs from C and D
    for c in C:
        for d in D:
            sum_cd = -(c + d)  # We need the negation to make the sum zero
            if sum_cd in sum_map:
                count += sum_map[sum_cd]  # Add the count from the hash map
                
    return count

# Example 1
A1 = [1, 2]
B1 = [-2, -1]
C1 = [-1, 2]
D1 = [0, 2]
print("Output:", fourSumCount(A1, B1, C1, D1))  # Expected Output: 2

# Example 2
A2 = [0]
B2 = [0]
C2 = [0]
D2 = [0]
print("Output:", fourSumCount(A2, B2, C2, D2))  # Expected Output: 1
