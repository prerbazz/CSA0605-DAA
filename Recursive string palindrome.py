def is_palindrome(s):
    # Base case: if the string is empty or has one character, it's a palindrome
    if len(s) <= 1:
        return True
    
    # Check if the first and last characters are the same
    if s[0] != s[-1]:
        return False
    
    # Recursive case: check the substring excluding the first and last characters
    return is_palindrome(s[1:-1])

# Example usage
string = "madam"
if is_palindrome(string):
    print(f"'{string}' is a palindrome")
else:
    print(f"'{string}' is not a palindrome")
  
