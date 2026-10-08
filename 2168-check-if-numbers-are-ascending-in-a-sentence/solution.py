class Solution(object):
    def areNumbersAscending(self, s):
        """
        :type s: str
        :rtype: bool
        """
        prev = -1

        for token in s.split():
            # 判斷 Token 是否全由數字組成
            if token.isdigit():
                curr = int(token)
                if curr <= prev:
                    return False
                prev = curr

        return True
