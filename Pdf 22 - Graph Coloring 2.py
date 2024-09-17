def is_valid_color(graph, color, vertex, c):
    """Check if it's valid to color vertex with color c"""
    for neighbor in graph[vertex]:
        if color[neighbor] == c:
            return False
    return True

def graph_coloring_util(graph, color, vertex, num_colors):
    """Recursive utility to solve the graph coloring problem"""
    if vertex == len(graph):
        return True
    
    for c in range(1, num_colors + 1):
        if is_valid_color(graph, color, vertex, c):
            color[vertex] = c
            if graph_coloring_util(graph, color, vertex + 1, num_colors):
                return True
            color[vertex] = 0
    return False

def find_min_colors(graph):
    """Find the minimum number of colors required to color the graph"""
    num_vertices = len(graph)
    color = [0] * num_vertices
    num_colors = 1

    while True:
        if graph_coloring_util(graph, color, 0, num_colors):
            return num_colors
        num_colors += 1

def maximize_colored_regions(num_colors, k):
    """Calculate the maximum number of regions you can color"""
    return (num_colors + 2) // k

edges = [(0, 1), (1, 2), (2, 3), (3, 0), (0, 2)]
num_vertices = 4

graph = [[] for _ in range(num_vertices)]
for u, v in edges:
    graph[u].append(v)
    graph[v].append(u)


min_colors = find_min_colors(graph)
print(f"Minimum number of colors required: {min_colors}")

k = 3
max_colored_regions = maximize_colored_regions(min_colors, k)
print(f"Maximum number of regions you can color: {max_colored_regions}")
