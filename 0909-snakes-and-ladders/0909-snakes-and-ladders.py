from collections import deque

class Solution:
    def snakesAndLadders(self, board: List[List[int]]) -> int:
        n=len(board)

        if n*n<=6 :
            return 1

        def get_val(sq):
            r = n - 1 - (sq - 1) // n
            c = (sq - 1) % n

            if (n - 1 - r) % 2 == 1:
                c = n - 1 - c

            return board[r][c]

        q=deque([(1,0)])# here first index is node and second index is number of moves
        visited=set([1])
        while q:
            node,moves=q.popleft()

            if node==n*n:
                return moves

            for i in range(1,7):
                if node+i>n*n:
                    continue
                next_node=node+i
                los=get_val(next_node) # los -> ladder or snake
                if los!=-1:
                    next_node=los
                if next_node not in visited:
                    visited.add(next_node)
                    q.append((next_node,moves+1))
        return -1


                    

        