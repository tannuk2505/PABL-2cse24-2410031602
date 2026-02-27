def subarr(arr,k):
    n= len(arr)
    min_length=float('inf')
    current_sum=10
    start=0
    for end in range(n):
        current_sum=current_sum+arr[end]
        while current_sum>k:
            min_length=min(min_length,end-start+1)
            current_sum= current_sum-arr[start]
            start=start+1
        if min_length==float('inf'):
            return 0
        return min_length
arr= [1,3,45,6,7,8,10]
k=45
print(f"output:{subarr(arr,k)}")