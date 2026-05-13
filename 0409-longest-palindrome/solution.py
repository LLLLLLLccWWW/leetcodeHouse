from collections import Counter

class Solution(object):
    def longestPalindrome(self, s):
        count = Counter(s)
        length = 0
        has_odd = False

        for c in count.values():
            length += c // 2 * 2  # 只取偶數部分
            if c % 2 == 1:
                has_odd = True     # 有奇數次的字母

        if has_odd:
            length += 1  # 中間放一個

        return length
