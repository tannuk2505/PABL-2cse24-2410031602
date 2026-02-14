def minJumps(arr):
    n = len(arr)
    
    # If array has 1 element
    if n <= 1:
        return 0
    
    # If first element is 0, we can't move
    if arr[0] == 0:
        return -1
    
    maxReach = arr[0]
    steps = arr[0]
    jumps = 1
    
    for i in range(1, n):
        
        # If we reached the last index
        if i == n - 1:
            return jumps
        
        maxReach = max(maxReach, i + arr[i])
        steps -= 1
        
        # If no more steps left
        if steps == 0:
            jumps += 1
            
            # If current index is beyond maxReach
            if i >= maxReach:
                return -1
            
            steps = maxReach - i
    
    return -1
arr = [1, 3, 5, 8, 9, 2, 6, 7, 6, 8, 9]
print(minJumps(arr))