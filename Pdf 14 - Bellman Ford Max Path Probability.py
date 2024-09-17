def maxProbability(n, edges, succProb, start, end):
    prob = [0.0] * n
    prob[start] = 1.0 
    
    
    for _ in range(n - 1):
        has_update = False
      
        for i, (u, v) in enumerate(edges):
            
            if prob[u] * succProb[i] > prob[v]:
                prob[v] = prob[u] * succProb[i]
                has_update = True
            if prob[v] * succProb[i] > prob[u]:
                prob[u] = prob[v] * succProb[i]
                has_update = True
        
        if not has_update:
            break
    
    return prob[end]


n = 3
edges = [[0, 1], [1, 2], [0, 2]]
succProb = [0.5, 0.5, 0.2]
start = 0
end = 2
print(maxProbability(n, edges, succProb, start, end))  # Output: 0.25


n = 3
edges = [[0, 1], [1, 2], [0, 2]]
succProb = [0.5, 0.5, 0.3]
start = 0
end = 2
print(maxProbability(n, edges, succProb, start, end))  # Output: 0.3


n = 3
edges = [[0, 1]]
succProb = [0.5]
start = 0
end = 2
print(maxProbability(n, edges, succProb, start, end))  # Output: 0.0
