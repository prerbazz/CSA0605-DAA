
MOUSE_WIN = 1
CAT_WIN = 2
DRAW = 0

def cat_mouse_game(graph):
    n = len(graph)
    
    dp = [[[DRAW] * 2 for _ in range(n)] for _ in range(n)]
    
    
    for i in range(1, n):
        dp[0][i][0] = dp[0][i][1] = MOUSE_WIN  
        dp[i][i][0] = dp[i][i][1] = CAT_WIN    
    
    
    degree = [[[0] * 2 for _ in range(n)] for _ in range(n)]
    
    
    for mouse in range(n):
        for cat in range(n):
            degree[mouse][cat][0] = len(graph[mouse]) 
            degree[mouse][cat][1] = len(graph[cat]) - (0 in graph[cat])  

    
    def backtrack(mouse, cat, turn):
        if turn == 0:  
            for prev_mouse in graph[mouse]:
                if dp[prev_mouse][cat][1] == DRAW:
                    if dp[mouse][cat][turn] == MOUSE_WIN:
                        dp[prev_mouse][cat][1] = MOUSE_WIN
                    else:
                        degree[prev_mouse][cat][1] -= 1
                        if degree[prev_mouse][cat][1] == 0:
                            dp[prev_mouse][cat][1] = CAT_WIN
        else:  
            for prev_cat in graph[cat]:
                if prev_cat == 0:  
                    continue
                if dp[mouse][prev_cat][0] == DRAW:
                    if dp[mouse][cat][turn] == CAT_WIN:
                        dp[mouse][prev_cat][0] = CAT_WIN
                    else:
                        degree[mouse][prev_cat][0] -= 1
                        if degree[mouse][prev_cat][0] == 0:
                            dp[mouse][prev_cat][0] = MOUSE_WIN
    
    
    queue = []
    
    
    for cat in range(1, n):
        for turn in range(2):
            queue.append((0, cat, turn))
    
    
    for pos in range(1, n):
        for turn in range(2):
            queue.append((pos, pos, turn))
    
    while queue:
        mouse, cat, turn = queue.pop(0)
        winner = dp[mouse][cat][turn]
        if turn == 0:  
            backtrack(mouse, cat, 1)
        else:  
            backtrack(mouse, cat, 0)
    
    return dp[1][2][0]  

graph = [[2,5],[3],[0,4,5],[1,4,5],[2,3],[0,2,3]]
print(cat_mouse_game(graph))  
graph = [[1,3],[0],[3],[0,2]]
print(cat_mouse_game(graph))
  
