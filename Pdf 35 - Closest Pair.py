def kClosest(points, k):
    # Sort points based on their squared distance from origin (0, 0)
    points.sort(key=lambda p: p[0]**2 + p[1]**2)
    
    # Return the first k points
    return points[:k]

# Example 1
points1 = [[1, 3], [-2, 2], [5, 8], [0, 1]]
k1 = 2
print("The", k1, "closest points are:", kClosest(points1, k1))  
# Expected Output: [[-2, 2], [0, 1]]

# Example 2
points2 = [[1, 3], [-2, 2]]
k2 = 1
print("The", k2, "closest point is:", kClosest(points2, k2))  
# Expected Output: [[-2, 2]]

# Example 3
points3 = [[3, 3], [5, -1], [-2, 4]]
k3 = 2
print("The", k3, "closest points are:", kClosest(points3, k3))  
# Expected Output: [[3, 3], [-2, 4]]

