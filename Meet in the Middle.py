def generate_subset_sums(arr):
    subset_sums = set()
    n = len(arr)
    
    num_subsets = 1 << n
    
    for i in range(num_subsets):
        current_sum = 0
        for j in range(n):
            if i & (1 << j):  # If the j-th bit is set in i, include arr[j] in the subset
                current_sum += arr[j]
        subset_sums.add(current_sum)
    
    return subset_sums

def meet_in_the_middle(arr, target):
    mid = len(arr) // 2
    left_part = arr[:mid]
    right_part = arr[mid:]

    left_sums = generate_subset_sums(left_part)
    right_sums = generate_subset_sums(right_part)

    for left_sum in left_sums:
        if (target - left_sum) in right_sums:
            return True

    return False

arr = [3, 34, 4, 12, 5, 2]
target = 9

result = meet_in_the_middle(arr, target)
print(f"Subset with sum {target} {'exists' if result else 'does not exist'}")
