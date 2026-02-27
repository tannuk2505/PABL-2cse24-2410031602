def min_swaps(arr, k):
    n = len(arr)
    
    # Step 1: Count elements <= k
    target_window_size = 0
    for x in arr:
        if x <= k:
            target_window_size += 1
            
    # Edge case: if no elements or all elements are <= k
    if target_window_size == 0:
        return 0

    # Step 2: Count "bad" elements (> k) in the first window
    bad = 0
    for i in range(target_window_size):
        if arr[i] > k:
            bad += 1
    
    ans = bad
    for i in range(target_window_size, n):
        if arr[i - target_window_size] > k:
            bad -= 1
        
        if arr[i] > k:
            bad += 1
            
        ans = min(ans, bad)
        
    return ans

arr = [2, 1, 5, 6, 3]
k = 3
print(f"Minimum swaps: {min_swaps(arr, k)}") 