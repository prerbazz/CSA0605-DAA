def subsets_with_element(E, x):
    E.sort()
    result = []
  
    def backtrack(start, current):
        if x in current:
            result.append(current[:])
        
      
        for i in range(start, len(E)):
            current.append(E[i])
            backtrack(i + 1, current)
            current.pop()
    
  
    backtrack(0, [])
    return result


E = [2, 3, 4, 5]
x = 3
print(subsets_with_element(E, x))  
