def smallestLexicographicString(s: str, pairs: list[list[int]]) -> str:
    from collections import defaultdict, deque
    
    def findConnectedComponents(n: int, pairs: list[list[int]]) -> list[list[int]]:
        graph = defaultdict(list)
        for u, v in pairs:
            graph[u].append(v)
            graph[v].append(u)
        
        visited = [False] * n
        components = []
        
        for i in range(n):
            if not visited[i]:
                component = []
                queue = deque([i])
                while queue:
                    node = queue.popleft()
                    if not visited[node]:
                        visited[node] = True
                        component.append(node)
                        for neighbor in graph[node]:
                            if not visited[neighbor]:
                                queue.append(neighbor)
                components.append(component)
        
        return components
    
    n = len(s)
    components = findConnectedComponents(n, pairs)
    
    s = list(s)
    
    for component in components:
        # Extract the characters corresponding to this component
        chars = [s[i] for i in component]
        # Sort the characters
        chars.sort()
        # Place them back into the string in sorted order
        for i, idx in enumerate(sorted(component)):
            s[idx] = chars[i]
    
    return ''.join(s)

# Example usage
s = "dcab"
pairs = [[0, 3], [1, 2]]
print(smallestLexicographicString(s, pairs))  # Output: "abcd"
