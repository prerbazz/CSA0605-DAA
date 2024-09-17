def wordBreak(s, wordDict):
    wordSet = set(wordDict)
    dp = [False] * (len(s) + 1)
    dp[0] = True  # An empty string can always be segmented
    
    # Fill the dp array
    for i in range(1, len(s) + 1):
        for j in range(i):
            if dp[j] and s[j:i] in wordSet:
                dp[i] = True
                break  # No need to check further if dp[i] is already True
    
    return dp[len(s)]
print(wordBreak("leetcode",["leet","code"]))
