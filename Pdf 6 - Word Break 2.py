def wordBreak(s, wordDict):
    wordSet = set(wordDict)
    dp = [False] * (len(s) + 1)
    dp[0] = True 
    for i in range(1, len(s) + 1):
        for j in range(i):
            if dp[j] and s[j:i] in wordSet:
                dp[i] = True
                break
    
    return dp[len(s)]

dictionary = {"i", "like", "sam", "sung", "samsung", "mobile", 
              "ice", "cream", "icecream", "man", "go", "mango"}

s1 = "ilike"
s2 = "ilikesamsung"

print("Yes" if wordBreak(s1, dictionary) else "No")  # Output: Yes
print("Yes" if wordBreak(s2, dictionary) else "No")  # Output: Yes
  
