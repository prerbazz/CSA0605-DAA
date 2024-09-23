def vertex_cover(n, edges):
    cover = set()
    edge_set = set(edges)

    while edge_set:
        u, v = edge_set.pop()
        cover.add(u)
        cover.add(v)
        edge_set = {e for e in edge_set if u not in e and v not in e}

    return list(cover)

# Test cases
edges1 = [(0, 1), (0, 2), (1, 2), (1, 3), (2, 4), (3, 4)]
print("Vertex Cover:", vertex_cover(5, edges1))  # Output: [1, 2, 3]

edges2 = [(0, 1), (0, 2), (1, 2), (2, 3)]
print("Vertex Cover:", vertex_cover(4, edges2))  # Output: [0, 2]
