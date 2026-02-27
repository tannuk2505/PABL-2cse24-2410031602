def searchInsert(nums, target):
    low = 0
    high = len(nums) - 1
    
    while low <= high:
        mid = (low + high) // 2
        
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
            
    return low

nums = [1, 3, 5, 6]
print(searchInsert(nums, 5)) # Output: 2 (Found)
print(searchInsert(nums, 2)) # Output: 1 (Not found, insert at index 1)
print(searchInsert(nums, 7)) # Output: 4 (Not found, insert at end) 