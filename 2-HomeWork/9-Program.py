def rotate(arr):
    n = len(arr)
    
    last = arr[n - 1]
    
    # Shift elements to the right
    for i in range(n - 1, 0, -1):
        arr[i] = arr[i - 1]
        
    arr[0] = last
    return arr
arr = [1, 2, 3, 4, 5]
print(rotate(arr))   # Output: [5, 1, 2, 3, 4]
