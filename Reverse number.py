def reverse_number(n, reversed_n=0):
    # Base case: when n becomes 0, return the reversed number
    if n == 0:
        return reversed_n
    
    # Recursive case: extract the last digit and build the reversed number
    reversed_n = reversed_n * 10 + n % 10
    return reverse_number(n // 10, reversed_n)

# Example usage
num = 12345
reversed_num = reverse_number(num)
print(f"The reversed number of {num} is {reversed_num}")
