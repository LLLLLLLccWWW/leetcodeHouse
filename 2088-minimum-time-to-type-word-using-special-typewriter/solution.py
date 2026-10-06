class Solution(object):
    def minTimeToType(self, word):
        """
        :type word: str
        :rtype: int
        """
        total_time = 0
        curr = 'a'

        for char in word:
            # 計算字母間的絕對差值
            diff = abs(ord(char) - ord(curr))
            # 取順時針與逆時針的最短距離，再加上打字的 1 秒
            total_time += min(diff,26 - diff) + 1
            # 更新當前指針位置
            curr = char

        return total_time
