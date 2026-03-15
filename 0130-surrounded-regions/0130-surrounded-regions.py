class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """

        m=len(board)
        n=len(board[0])

        check=set()

        def dfs(r,c):
            if r< 0 or r>=m or c<0 or c>=n:
                return
            if board[r][c]!='O' or (r,c) in check:
                return
            
            check.add((r,c))

            dfs(r-1,c)
            dfs(r+1,c)
            dfs(r,c-1)
            dfs(r,c+1)
            

        for i in range(m):
            for j in range(n):
                if i==0 or j==0 or i==(m-1) or j==(n-1):
                    if board[i][j] =='O' and (i,j) not in check:
                        dfs(i,j)
        for i in range(m):
            for j in range(n):
                if board[i][j]=='O' and (i,j) not in check:
                    board[i][j]='X'