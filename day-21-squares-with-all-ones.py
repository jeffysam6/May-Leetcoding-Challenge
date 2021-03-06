class Solution:
    def countSquares(self, matrix: List[List[int]]) -> int:
        ans = 0

        for i in range(len(matrix)):
            for j in range(len(matrix[0])):

                if(matrix[i][j] == 1):

                    if(i == 0 or j == 0):
                        ans += 1

                    else:
                        temp = min(matrix[i-1][j],matrix[i][j-1],matrix[i-1][j-1]) + 1
                        matrix[i][j] = temp
                        ans += temp


        return ans
