def getMinDiff(arr, k):
    n = len(arr)
    if n == 1:
        return 0
    
    arr.sort()
    
    ans = arr[n-1] - arr[0]
    

    for i in range(n - 1):
        if arr[i+1] < k:
            continue
            
        max_h = max(arr[n-1] - k, arr[i] + k)
        min_h = min(arr[0] + k, arr[i+1] - k)
        

        ans = min(ans, max_h - min_h)
        
    return ans