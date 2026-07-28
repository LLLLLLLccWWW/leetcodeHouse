class Solution(object):
    def numRookCaptures(self, board):
        """
        :type board: List[List[str]]
        :rtype: int
        """
        r,c = 0,0

        for i in range(8):
            for j in range(8):
                if board[i][j] == 'R':
                    r,c = i,j
                    break

        captures = 0

        directions = [(-1,0),(1,0),(0,-1),(0,1)]

        for dr,dc in directions:
            nr,nc = r + dr, c + dc
            while 0 <= nr < 8 and 0 <= nc < 8:
                if board[nr][nc] == 'p':
                    captures += 1
                    break
                elif board[nr][nc] == 'B':
                    break

                nr += dr
                nc += dc

        return captures
