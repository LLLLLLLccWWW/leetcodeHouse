class Solution(object):
    def halvesAreAlike(self, s):
        """
        :type s: str
        :rtype: bool
        """
        vowels = set('aeiouAEIOU')
        n = len(s)
        mid = n // 2

        # 分別統計前半段與後半段的母音個數
        count_a = sum(1 for char in s[:mid] if char in vowels)
        count_b = sum(1 for char in s[mid:] if char in vowels)

        return count_a == count_b
