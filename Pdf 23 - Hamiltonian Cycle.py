def is_valid(v, pos, path, graph):
    """Check if the current vertex v can be added at index pos in the Hamiltonian Path."""
    if graph[path[pos - 1]][v] == 0:
        return False
    if v in path:
        return False
    return True

def hamiltonian_cycle_util(graph, path, pos):
    """Recursive utility function to solve the Hamiltonian Cycle problem."""
    n = len(graph)
    if pos == n:
        return graph[path[pos - 1]][path[0]] == 1
    
    for v in range(1, n):
        if is_valid(v, pos, path, graph):
            path[pos] = v
            if hamiltonian_cycle_util(graph, path, pos + 1):
                return True
            path[pos] = -1
    return False

def find_hamiltonian_cycle(edges, n):
    """Check if there exists a Hamiltonian Cycle in the graph."""
    # Create adjacency matrix
    graph = [[0] * n for _ in range(n)]
    for u, v in edges:
        graph[u][v] = 1
        graph[v][u] = 1
    
    path = [-1] * n
    
    path[0] = 0
    
    if hamiltonian_cycle_util(graph, path, 1):
        return True
    return False

edges = [(0, 1), (1, 2), (2, 3), (3, 0), (0, 2), (2, 4), (4, 0)]
n = 5
print("Hamiltonian Cycle exists:" if find_hamiltonian_cycle(edges, n) else "No Hamiltonian Cycle exists.")
