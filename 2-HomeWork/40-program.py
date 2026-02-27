def subsets(nums):
    result = []
    subset = []
    
    def backtrack(i):
        if i >= len(nums):
            result.append(list(subset))
            return
        
        subset.append(nums[i])
        backtrack(i + 1)
        
        subset.pop()
        backtrack(i + 1)
        
    backtrack(0)
    return result

nums = [1, 2, 3]
print(subsets(nums))