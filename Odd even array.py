def arrange_odd_even(nums):
    odd = []
    even = []

    # Separate the odd and even numbers
    for num in nums:
        if num % 2 == 0:
            even.append(num)
        else:
            odd.append(num)
    
    # Check if there are enough odd and even numbers
    n = len(nums)
    half_n = n // 2
    if len(odd) < half_n or len(even) < half_n:
        raise ValueError("Not enough odd or even numbers to satisfy the requirement")

    # Create the result array with half odd and half even numbers
    result = []
    result.extend(odd[:half_n])
    result.extend(even[:half_n])

    return result

# Example usage
nums = [1, 2, 3, 4, 5, 6]
arranged = arrange_odd_even(nums)
print("Arranged array:", arranged)
