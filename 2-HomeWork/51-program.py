class Solution:
    def prefixSumMatrix(self, mat):
        n = len(mat)
        m = len(mat[0])

        # Create prefix matrix
        prefix = [[0]*m for _ in range(n)]

        for i in range(n):
            for j in range(m):
                prefix[i][j] = mat[i][j]

                if i > 0:
                    prefix[i][j] += prefix[i-1][j]

                if j > 0:
                    prefix[i][j] += prefix[i][j-1]

                if i > 0 and j > 0:
                    prefix[i][j] -= prefix[i-1][j-1]

        return prefix

mat = [
    [1, 2],
    [3, 4]
]

obj = Solution()
print(obj.prefixSumMatrix(mat))