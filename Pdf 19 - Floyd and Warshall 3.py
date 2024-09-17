def floyd_warshall(n, edges):
    dist = [[float('inf')] * n for _ in range(n)]
    
    for i in range(n):
        dist[i][i] = 0
    
    for u, v, w in edges:
        dist[u][v] = w
    
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

n = 4
edges = [
    [0, 1, 3],  # City 1 to City 2: 3
    [0, 2, 8],  # City 1 to City 3: 8
    [0, 3, -4], # City 1 to City 4: -4
    [1, 2, 4],  # City 2 to City 3: 4
    [1, 3, 1],  # City 2 to City 4: 1
    [2, 3, -5], # City 3 to City 4: -5
    [2, 1, 6],  # City 3 to City 2: 6
    [3, 1, 2],  # City 4 to City 2: 2
    [3, 2, 1]   # City 4 to City 3: 1
]

dist_matrix = floyd_warshall(n, edges)
print("Distance Matrix before applying Floyd-Warshall Algorithm:")
print_matrix(dist_matrix)

print("Distance Matrix after applying Floyd-Warshall Algorithm:")
print_matrix(dist_matrix)

print(f"City 1 to City 3 = {dist_matrix[0][2]}")

n = 6
edges = [
    [0, 1, 1],  # Router A to Router B: 1
    [0, 2, 5],  # Router A to Router C: 5
    [1, 2, 2],  # Router B to Router C: 2
    [1, 3, 1],  # Router B to Router D: 1
    [2, 4, 3],  # Router C to Router E: 3
    [3, 4, 1],  # Router D to Router E: 1
    [3, 5, 6],  # Router D to Router F: 6
    [4, 5, 2]   # Router E to Router F: 2
]

dist_matrix = floyd_warshall(n, edges)
print("\nDistance Matrix after applying Floyd-Warshall Algorithm (Test Case b):")
print_matrix(dist_matrix)

print(f"Router A to Router C = {dist_matrix[0][2]}")
