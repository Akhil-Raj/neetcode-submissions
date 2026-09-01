class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        # [i, j] - > [j, n - 1 - i] -> [n - 1 - i, n - 1 - j] -> [n - 1 - j, i] -> [i, j]
        n = len(matrix)
        for i in range((len(matrix) + 1) // 2):
            for j in range(len(matrix[0]) // 2):
                temp = matrix[j][n - 1 - i]
                matrix[j][n - 1 - i] = matrix[i][j]
                temp2 = matrix[n - 1 - i][n - 1 - j]
                matrix[n - 1 - i][n - 1 - j] = temp
                temp = matrix[n - 1 - j][i]
                matrix[n - 1 - j][i] = temp2
                matrix[i][j] = temp
        
        print(matrix)