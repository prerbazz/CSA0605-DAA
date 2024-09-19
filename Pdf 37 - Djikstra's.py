import heapq

# Function to implement Dijkstra's Algorithm
def dijkstra(n, graph, source):
    # Distance list to store the minimum distance from the source to each vertex
    dist = [float('inf')] * n
    dist[source] = 0
    
    # Min-heap priority queue to pick the vertex with the minimum distance
    pq = [(0, source)]  # (distance, vertex)
    
    while pq:
        current_dist, u = heapq.heappop(pq)
        
        # If the current distance is greater than the recorded distance, continue
        if current_dist > dist[u]:
            continue
        
        # Relaxation step: explore the neighbors of the current vertex
        for v in range(n):
            if graph[u][v] != float('inf'):  # If there's an edge from u to v
                new_dist = dist[u] + graph[u][v]
                if new_dist < dist[v]:
                    dist[v] = new_dist
                    heapq.heappush(pq, (new_dist, v))
    
    return dist

# Test Case 1
n1 = 5
graph1 = [[0, 10, 3, float('inf'), float('inf')],
          [float('inf'), 0, 1, 2, float('inf')],
          [float('inf'), 4, 0, 8, 2],
          [float('inf'), float('inf'), float('inf'), 0, 7],
          [float('inf'), float('inf'), float('inf'), 9, 0]]
source1 = 0
output1 = dijkstra(n1, graph1, source1)

# Test Case 2
n2 = 4
graph2 = [[0, 5, float('inf'), 10],
          [float('inf'), 0, 3, float('inf')],
          [float('inf'), float('inf'), 0, 1],
          [float('inf'), float('inf'), float('inf'), 0]]
source2 = 0
output2 = dijkstra(n2, graph2, source2)

output1, output2
