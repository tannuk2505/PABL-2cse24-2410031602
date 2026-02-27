def plusOne(digits):
    n = len(digits)
    
    # Traverse from right to left
    for i in range(n - 1, -1, -1):
        # Increment the current digit
        digits[i] += 1
        
        # If the digit is < 10, no more carry is needed
        if digits[i] < 10:
            return digits
        
        # If the digit is 10, set it to 0 and continue to the next digit
        digits[i] = 0
        
    # If we reach here, it means all digits were 9
    # e.g., [9, 9] -> [0, 0]. We need to prepend 1.
    return [1] + digits

# Example Cases:
print(plusOne([1, 2, 3])) # Output: [1, 2, 4]
print(plusOne([4, 3, 2, 9])) # Output: [4, 3, 3, 0]
print(plusOne([9, 9, 9])) # Output: [1, 0, 0, 0]