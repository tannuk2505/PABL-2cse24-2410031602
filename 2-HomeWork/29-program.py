from bisect import bisect_right

def findMedian(mat):
    n = len(mat)
    m = len(mat[0])
    
    low = min(mat[i][0] for i in range(n))
    high = max(mat[i][m-1] for i in range(n))
    
    target_count = (n * m) // 2 + 1
    
    while low <= high:
        mid = (low + high) // 2
        count = 0
        
        for i in range(n):
            count += bisect_right(mat[i], mid)
            
        if count < target_count:
            low = mid + 1
        else:
            high = mid - 1
            
    return low

matrix = [
    [1, 3, 5],
    [2, 6, 9],
    [3, 6, 9]
]
print(f"The median is: {findMedian(matrix)}") # Output: 5