def is_palindrome(s: str) -> bool:
    # Initialize left and right pointers
    left = 0
    right = len(s) - 1
    
    # While the pointers have not met or crossed each other
    while left < right:
        # If the characters at the pointers are not equal, return False
        if s[left] != s[right]:
            return False
        # Move the pointers one position towards the center
        left += 1
        right -= 1
        
    # If the loop ends, the string is a palindrome
    return True
word = input("Enter a word:")
x = is_palindrome(word)
print(x)
