class Solution(object):
    def minimumMoves(self, s):
        """
        :type s: str
        :rtype: int
        """
        moves = 0
        i = 0
        n = len(s)

        while i < n:
            if s[i] == 'X':
                moves += 1
                i += 3  # 貪婪轉換連續三個字元，指針直接跳 3 格
            else:
                i += 1

        return moves

