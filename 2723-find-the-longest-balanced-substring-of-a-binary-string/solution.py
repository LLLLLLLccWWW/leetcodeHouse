class Solution:
    def findTheLongestBalancedSubstring(self, s: str) -> int:
        max_len = 0
        zeros = 0
        ones = 0

        for ch in s:
            if ch == '0':
                # 若之前已開始累計 '1'，代表進入新的 "0...01...1" 區段，重置計數
                if ones > 0:
                    zeros = 0
                    ones = 0
                zeros += 1
            else:
                ones += 1
                max_len = max(max_len,2 * min(zeros,ones))

        return max_len
