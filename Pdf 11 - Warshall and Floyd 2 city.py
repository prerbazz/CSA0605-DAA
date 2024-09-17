def findTheCity(n, edges, distanceThreshold):
    
    INF = 10**9
    
    dist = [[INF] * n for _ in range(n)]
    

    for i in range(n):
        dist[i][i] = 0
    

    for u, v, w in edges:
        dist[u][v] = w
        dist[v][u] = w
    
    for k in range(n):
        for i in range(n):
            for j in range(n):
                dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])
    
    city_with_min_reachable = -1
    min_reachable_count = INF
    
    for i in range(n):
        reachable_count = 0
        for j in range(n):
            if dist[i][j] <= distanceThreshold:
                reachable_count += 1
        
        if reachable_count <= min_reachable_count:
            min_reachable_count = reachable_count
            city_with_min_reachable = i
    
    return city_with_min_reachable


n1 = 4
edges1 = [[0,1,3],[1,2,1],[1,3,4],[2,3,1]]
distanceThreshold1 = 4
print(findTheCity(n1, edges1, distanceThreshold1)) 

n2 = 5
edges2 = [[0,1,2],[0,4,8],[1,2,3],[1,4,2],[2,3,1],[3,4,1]]
distanceThreshold2 = 2
print(findTheCity(n2, edges2, distanceThreshold2))  
