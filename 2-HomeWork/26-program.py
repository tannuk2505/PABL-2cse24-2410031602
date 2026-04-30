ef spiralOrder(matrix):
    if not matrix:
        return []
    
    n = len(matrix)
    m = len(matrix[0])
    
    top, bottom = 0, n - 1
    left, right = 0, m - 1
    result = []
    
    while top <= bottom and left <= right:
        for j in range(left, right + 1):
            result.append(matrix[top][j])
        top += 1
        
        for i in range(top, bottom + 1):
            result.append(matrix[i][right])
        right -= 1
        
        if top <= bottom:
            for j in range(right, left - 1, -1):
                result.append(matrix[bottom][j]);