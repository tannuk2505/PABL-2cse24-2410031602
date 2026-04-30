class Solution:
    def checkDiff(self, arr, k):
        s = set(arr)

        for x in arr:
            if (x - k) in s and (x - k) != x:
                return True

        return False
    
arr = [5, 3, 7, 1]
k = 2

obj = Solution()
print(obj.checkDiff(arr, k))