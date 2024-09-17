def numIdenticalPairs(nums):
    count_map = {}
    good_pairs = 0
    
    for num in nums:
        if num in count_map:
            good_pairs += count_map[num]
            count_map[num] += 1
        else:
            count_map[num] = 1
    
    return good_pairs

print(numIdenticalPairs([1, 2, 3, 1, 1, 3]))  
print(numIdenticalPairs([1, 1, 1, 1]))        
print(numIdenticalPairs([1, 2, 3]))        
