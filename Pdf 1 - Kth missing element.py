def findKthPositive(arr, k):
    for i in range(len(arr)):
        missing = arr[i] - (i + 1)
        if missing >= k:
            return i + k
    return len(arr) + k
print(findKthPositive([2,3,4,6,8],2))
