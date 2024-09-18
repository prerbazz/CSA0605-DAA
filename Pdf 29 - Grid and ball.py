def find_ways(m, n, N, i, j):
    # Initialize a 3D dp array with dimensions (N+1) x m x n
    dp = [[[0 for _ in range(n)] for _ in range(m)] for _ in range(N + 1)]
    
    # Initialize the result
    result = 0
    
    # Direction vectors for moving up, down, left, and right
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    
    # Base case: 0 steps, no way to get out
    dp[0][i][j] = 1
    
    # Iterate through each number of steps
    for step in range(1, N + 1):
        for x in range(m):
            for y in range(n):
                for dx, dy in directions:
                    new_x, new_y = x + dx, y + dy
                    # If the new position is out of the grid, increment the result
                    if new_x < 0 or new_x >= m or new_y < 0 or new_y >= n:
                        result += dp[step - 1][x][y]
                    else:
                        dp[step][new_x][new_y] += dp[step - 1][x][y]
    
    return result

# Example Usage:
m1, n1, N1, i1, j1 = 2, 2, 2, 0, 0
print("Output for m=2, n=2, N=2, i=0, j=0:", find_ways(m1, n1, N1, i1, j1))  # Output: 6

m2, n2, N2, i2, j2 = 1, 3, 3, 0, 1
print("Output for m=1, n=3, N=3, i=0, j=1:", find_ways(m2, n2, N2, i2, j2))  # Output: 1
