from collections import defaultdict
import heapq

# Function to implement Dijkstra's Algorithm for an edge list
def dijkstra_edge_list(n, edges, source, target):
    # Create adjacency list from edge list
    graph = defaultdict(list)
    for u, v, w in edges:
        graph[u].append((v, w))
        graph[v].append((u, w))  # Assuming undirected graph for this case
    
    # Distance list to store the minimum distance from the source to each vertex
    dist = [float('inf')] * n
    dist[source] = 0
    
    # Min-heap priority queue to pick the vertex with the minimum distance
    pq = [(0, source)]  # (distance, vertex)
    
    while pq:
        current_dist, u = heapq.heappop(pq)
        
        # If we reached the target, return the distance
        if u == target:
            return current_dist
        
        # If the current distance is greater than the recorded distance, continue
        if current_dist > dist[u]:
            continue
        
        # Explore the neighbors of the current vertex
        for v, w in graph[u]:
            new_dist = dist[u] + w
            if new_dist < dist[v]:
                dist[v] = new_dist
                heapq.heappush(pq, (new_dist, v))
    
    return dist[target]

# Test Case 1
n1 = 6
edges1 = [(0, 1, 7), (0, 2, 9), (0, 5, 14),
          (1, 2, 10), (1, 3, 15),
          (2, 3, 11), (2, 5, 2),
          (3, 4, 6), (4, 5, 9)]
source1 = 0
target1 = 4
output1 = dijkstra_edge_list(n1, edges1, source1, target1)
print(f"Test Case 1 Output: {output1}")

# Test Case 2
n2 = 5
edges2 = [(0, 1, 10), (0, 4, 3),
          (1, 2, 2), (1, 4, 4),
          (2, 3, 9), (3, 2, 7),
          (4, 1, 1), (4, 2, 8), (4, 3, 2)]
source2 = 0
target2 = 3
output2 = dijkstra_edge_list(n2, edges2, source2, target2)
print(f"Test Case 2 Output: {output2}")
