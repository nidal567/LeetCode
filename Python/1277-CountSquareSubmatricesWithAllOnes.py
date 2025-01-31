class Solution:
    def countSquares(self, matrix: List[List[int]]) -> int:
        # Need the dimensions of the matrix
        n, m = len(matrix), len(matrix[0]) # row, col

        # Create a DP table with same dimensions as matrix
        dp = [[0] * m for _ in range(n)] 

        ans = 0     # Total count of squares

        # We initialize first row of DP table
        for i in range(n):
            dp[i][0] = matrix[i][0]
            ans += dp[i][0]

        # Initialize first column of DP table
        for j in range(1, m):
            dp[0][j] = matrix[0][j]
            ans += dp[0][j]
        
        # Fill DP table for remaining cells
        for i in range(1, n):
            for j in range(1, m):
                if matrix[i][j] == 1: # only if curr cell is 1
                    # Find minimum of left, top, diag cells and add 1
                    dp[i][j] = 1 + min(dp[i][j-1], dp[i-1][j], dp[i-1][j-1])
                ans += dp[i][j]
        
        return ans