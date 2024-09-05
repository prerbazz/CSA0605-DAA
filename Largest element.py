def max_ele(arr):
    maxi=arr[0]
    for ele in arr:
        if ele>maxi:
            maxi=ele
    return maxi
arr=[10,24,36,7,8,9,45]
print("Largest element of array=",max_ele(arr))
