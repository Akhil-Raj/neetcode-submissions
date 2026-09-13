class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        up = [[0 for i in range(n + 1)] for j in range(m + 1)]
        for col in range(1, n + 1):
            up[1][col] = 1
        for row in range(1, m + 1):
            up[row][1] = 1
        
        for row in range(2, m + 1):
            for col in range(2, n + 1):
                up[row][col] = up[row - 1][col] + up[row][col - 1]
            
        return up[m][n]