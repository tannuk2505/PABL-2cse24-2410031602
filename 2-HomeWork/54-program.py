class Solution:
    def prevSmaller(self, arr):
        stack = []
        result = []

        for x in arr:
            while stack and stack[-1] >= x:
                stack.pop()

            if stack:
                result.append(stack[-1])
            else:
                result.append(-1)

            stack.append(x)

        return result

arr = [1, 5, 0, 3, 4, 5]

obj = Solution()
print(obj.prevSmaller(arr))