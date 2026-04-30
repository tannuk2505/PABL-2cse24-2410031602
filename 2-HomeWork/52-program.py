class Solution:
    def footpath(self, n, m, a, queries):
        # Step 1: Create DP arrays
        topl = [[0]*m for _ in range(n)]
        topr = [[0]*m for _ in range(n)]
        bottoml = [[0]*m for _ in range(n)]
        bottomr = [[0]*m for _ in range(n)]

        # Top-left
        for i in range(n):
            for j in range(m):
                topl[i][j] = a[i][j]
                if i > 0:
                    topl[i][j] = min(topl[i][j], topl[i-1][j])
                if j > 0:
                    topl[i][j] = min(topl[i][j], topl[i][j-1])

        # Top-right
        for i in range(n):
            for j in range(m-1, -1, -1):
                topr[i][j] = a[i][j]
                if i > 0:
                    topr[i][j] = min(topr[i][j], topr[i-1][j])
                if j < m-1:
                    topr[i][j] = min(topr[i][j], topr[i][j+1])

        # Bottom-left
        for i in range(n-1, -1, -1):
            for j in range(m):
                bottoml[i][j] = a[i][j]
                if i < n-1:
                    bottoml[i][j] = min(bottoml[i][j], bottoml[i+1][j])
                if j > 0:
                    bottoml[i][j] = min(bottoml[i][j], bottoml[i][j-1])

        # Bottom-right
        for i in range(n-1, -1, -1):
            for j in range(m-1, -1, -1):
                bottomr[i][j] = a[i][j]
                if i < n-1:
                    bottomr[i][j] = min(bottomr[i][j], bottomr[i+1][j])
                if j < m-1:
                    bottomr[i][j] = min(bottomr[i][j], bottomr[i][j+1])

        # Step 2: Answer queries
        result = []

        for r, c in queries:
            r -= 1
            c -= 1

            tl = topl[r-1][c-1] if r > 0 and c > 0 else 0
            tr = topr[r-1][c+1] if r > 0 and c < m-1 else 0
            bl = bottoml[r+1][c-1] if r < n-1 and c > 0 else 0
            br = bottomr[r+1][c+1] if r < n-1 and c < m-1 else 0

            result.append(tl + tr + bl + br)

        return result

# Input
n = 3
m = 3

a = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

queries = [(2, 2), (1, 1)]

# Call function
obj = Solution()
result = obj.footpath(n, m, a, queries)

print(result)
