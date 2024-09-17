INF = float('inf')

def network_delay_time(times, n, k):
    dist = [[INF] * n for _ in range(n)]
    
    # Distance to self is 0
    for i in range(n):
        dist[i][i] = 0
    
    for u, v, w in times:
        dist[u-1][v-1] = w  
    
    for t in range(n):
        for i in range(n):
            for j in range(n):
                dist[i][j] = min(dist[i][j], dist[i][t] + dist[t][j])
    
    
    result = max(dist[k-1])
    
    return result if result < INF else -1

times = [[2, 1, 1], [2, 3, 1], [3, 4, 1]]
n = 4
k = 2
print(network_delay_time(times, n, k))  
