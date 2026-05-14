class Solution(object):
    def tictactoe(self, moves):
        board = [['' for _ in range(3)] for _ in range(3)]
        
        # 把棋子放上棋盤
        for i, (r, c) in enumerate(moves):
            board[r][c] = 'A' if i % 2 == 0 else 'B'
        
        # 檢查獲勝條件
        def check(player):
            # 檢查3行
            for r in range(3):
                if all(board[r][c] == player for c in range(3)):
                    return True
            # 檢查3列
            for c in range(3):
                if all(board[r][c] == player for r in range(3)):
                    return True
            # 檢查對角線
            if all(board[i][i] == player for i in range(3)):
                return True
            if all(board[i][2-i] == player for i in range(3)):
                return True
            return False
        
        if check('A'): return 'A'
        if check('B'): return 'B'
        if len(moves) == 9: return 'Draw'
        return 'Pending'
