class WordFilter:
    def __init__(self, words):
        self.lookup = {}
        for index, word in enumerate(words):
            n = len(word)
            for i in range(n + 1):
                for j in range(n + 1):
                    prefix = word[:i]
                    suffix = word[j:]
                    self.lookup[prefix + '#' + suffix] = index

    def f(self, pref, suff):
        return self.lookup.get(pref + '#' + suff, -1)

wordFilter = WordFilter(["apple", "banana", "grape", "melon"])

print(wordFilter.f("a", "e"))    
print(wordFilter.f("ba", "a"))   
print(wordFilter.f("gr", "e"))   
print(wordFilter.f("me", "on"))  
print(wordFilter.f("x", "y"))   
                  
