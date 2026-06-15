def reverseString(s):
    # Start from both ends
    left = 0
    right = len(s) - 1
    
    # Move towards middle, swapping
    while left < right:
        s[left], s[right] = s[right], s[left]
        left += 1
        right -= 1
    
    return s
# Example 1
s = ["h", "e", "l", "l", "o"]
print(reverseString(s))  # Should print ["o", "l", "l", "e", "h"]

# Example 2
s = ["H", "a", "n", "n", "a", "h"]
print(reverseString(s))  # Should print ["h", "a", "n", "n", "a", "H"]