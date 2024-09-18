def subsets(S):
    
    S.sort()
    result = []

    def backtrack(start, current):
        result.append(current[:])
        for i in range(start, len(S)):
            
            if i > start and S[i] == S[i - 1]:
                continue
          
            current.append(S[i])
            backtrack(i + 1, current)
            
            current.pop()
    
    
    backtrack(0, [])
    return result

A = [1, 2, 3]
print(subsets(A))  



B = [1, 2, 2]
print(subsets(B))  
