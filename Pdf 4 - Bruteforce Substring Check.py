def stringMatching(words):
    result = []
    
    # Iterate through each word
    for i in range(len(words)):
        # Compare the current word with every other word
        for j in range(len(words)):
            # Avoid comparing the word with itself and check if it's a substring
            if i != j and words[i] in words[j]:
                result.append(words[i])
                break  # No need to check further if we found a match
    
    return result
print(stringMatching(["superhero","super","hello","hell"]))
