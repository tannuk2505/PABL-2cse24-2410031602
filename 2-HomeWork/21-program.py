def mindeff_choclates(arr,m):
    n= len(arr)
    if m==0 or n==0:
        return 0
    if m>n:
        return 0
    arr.sort()
    min_diff= float('inf')
    for i in range(n-m+1):
        diff=arr[i+m-1]-arr[i]
        min_diff=min(min_diff,diff)  
    return min_diff     
arr=[3,4,5,6,7,8,9,10]
m=5
print(f"output:{mindeff_choclates(arr,m)}")