class Solution:
    def min_sprinklers(self, gallery, n):
        intervals = []

        # Step 1: Convert into intervals
        for i in range(n):
            if gallery[i] != -1:
                left = max(0, i - gallery[i])
                right = min(n - 1, i + gallery[i])
                intervals.append((left, right))

        # Step 2: Sort intervals by left
        intervals.sort()

        # Step 3: Greedy coverage
        count = 0
        i = 0
        target = 0

        while target < n:
            max_reach = -1

            while i < len(intervals) and intervals[i][0] <= target:
                max_reach = max(max_reach, intervals[i][1])
                i += 1

            if max_reach < target:
                return -1

            count += 1
            target = max_reach + 1

        return count
    
gallery = [-1, 2, 2, -1, 0, 0]
n = len(gallery)

obj = Solution()
print(obj.min_sprinklers(gallery, n))