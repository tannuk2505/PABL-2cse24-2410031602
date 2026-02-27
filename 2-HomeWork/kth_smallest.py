def minSwaps(arr, k):
    n = len(arr)
    
    # Step 1: Count elements <= k
    good = sum(1 for x in arr if x <= k)
    
    # Step 2: Count bad elements in first window
    bad = sum(1 for i in range(good) if arr[i] > k)
    
    ans = bad
    i = 0
    
    # Step 3: Slide the window
    for j in range(good, n):
        
        # Remove left element
        if arr[i] > k:
            bad -= 1
        
        # Add right element
        if arr[j] > k:
            bad += 1
        
        ans = min(ans, bad)
        i += 1
    
    return ans