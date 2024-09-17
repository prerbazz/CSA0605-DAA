def floyd_warshall(n, edges):
    dist = [[float('inf')] * n for _ in range(n)]
    
    for i in range(n):
        dist[i][i] = 0
    
    for u, v, w in edges:
        dist[u][v] = w
    
    # Floyd-Warshall Algorithm
    for k in range(n):
        for i in range(n):
            for j in range(n):
                if dist[i][k] + dist[k][j] < dist[i][j]:
                    dist[i][j] = dist[i][k] + dist[k][j]

    return dist

def print_matrix(matrix):
    print("Distance Matrix:")
    for row in matrix:
        print(" ".join(f"{x:6}" if x != float('inf') else "  inf" for x in row))

# Test case
n = 5
edges = [
    [0, 1, 2],  # City 0 to City 1: 2
    [0, 4, 8],  # City 0 to City 4: 8
    [1, 2, 3],  # City 1 to City 2: 3
    [1, 4, 2],  # City 1 to City 4: 2
    [2, 3, 1],  # City 2 to City 3: 1
    [3, 4, 1]   # City 3 to City 4: 1
]

dist_matrix = floyd_warshall(n, edges)
print("Distance Matrix after applying Floyd-Warshall Algorithm:")
print_matrix(dist_matrix)

print(f"\nShortest path from City 0 to City 1 = {dist_matrix[0][1]}")
print(f"Shortest path from City 1 to City 4 = {dist_matrix[1][4]}")
print(f"Shortest path from City 2 to City 3 = {dist_matrix[2][3]}")
print(f"Shortest path from City 3 to City 4 = {dist_matrix[3][4]}")


print("\nTest Case Results:")

print(f"Shortest path from City 2 to City 0 = {dist_matrix[2][0]}")

print(f"Shortest path from City 4 to City 2 = {dist_matrix[4][2]}")


edges = [
    [2, 0, 2],  # C to A: 2
    [0, 1, 4],  # A to B: 4
    [1, 2, 1],  # B to C: 1
    [1, 4, 6],  # B to E: 6
    [4, 0, 1],  # E to A: 1
    [0, 3, 5],  # A to D: 5
    [3, 4, 2],  # D to E: 2
    [4, 3, 4],  # E to D: 4
    [3, 2, 1],  # D to C: 1
    [2, 3, 3]   # C to D: 3
]


dist_matrix = floyd_warshall(n, edges)
print("\nDistance Matrix after applying Floyd-Warshall Algorithm for additional test cases:")
print_matrix(dist_matrix)


print(f"Shortest path from City 4 to City 2 = {dist_matrix[4][2]}")
