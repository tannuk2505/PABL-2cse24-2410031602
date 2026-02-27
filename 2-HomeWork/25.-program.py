def is_palindrome_number(n):
    if n < 0:
        return False
        
    original = n
    reversed_num = 0
    
    while n > 0:
        digit = n % 10
        reversed_num = reversed_num * 10 + digit
        n //= 10
        
    return original == reversed_num

def check_all_palindromes(arr):
    for num in arr:
        if not is_palindrome_number(num):
            return False
    return True

arr1 = [121, 131, 202]
arr2 = [121, 131, 45]

print(f"Array 1 result: {check_all_palindromes(arr1)}") # Output: True
print(f"Array 2 result: {check_all_palindromes(arr2)}") # Output: False