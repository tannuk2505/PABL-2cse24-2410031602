import heapq

class Solution:
    def minSteps(self, arr):
        # Step 1: Calculate total sum
        total = sum(arr)
        target = total / 2

        # Step 2: Max heap (use negative values)
        max_heap = [-x for x in arr]
        heapq.heapify(max_heap)

        steps = 0

        # Step 3: Reduce sum
        while total > target:
            largest = -heapq.heappop(max_heap)
            
            half = largest / 2
            total -= half
            
            heapq.heappush(max_heap, -half)
            steps += 1

        return steps

arr = [8, 6, 2]

obj = Solution()
print(obj.minSteps(arr))