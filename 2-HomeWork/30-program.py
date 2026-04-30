def rowWithMax1s(arr):
    n = len(arr)
    m = len(arr[0])
    
    max_row_idx = -1
    row = 0
    col = m - 1
    
    while row < n and col >= 0:
        if arr[row][col] == 1:
            max_row_idx = row
            col -= 1
        else:
            row += 1
            
    return max_row_idx

matrix = [
    [0, 1, 1, 1],
    [0, 0, 1, 1],
    [1, 1, 1, 1],
    [0, 0, 0, 0]
]
print(f"Row with max 1s: {rowWithMax1s(matrix)}") # Output: 2