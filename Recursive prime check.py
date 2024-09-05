def is_prime(n, i=2):
    # Base cases
    if n <= 2:
        return True if n == 2 else False
    if n % i == 0:
        return False
    if i * i > n:
        return True
    
    # Recursive case
    return is_prime(n, i + 1)

# Example usage
num = 29
if is_prime(num):
    print(f"{num} is a prime number")
else:
    print(f"{num} is not a prime number")
  
