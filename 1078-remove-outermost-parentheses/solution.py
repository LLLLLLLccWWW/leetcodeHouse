class Solution(object):
    def removeOuterParentheses(self, s):
        """
        :type s: str
        :rtype: str
        """
        res = []
        opened = 0

        for char in s:
            if char == '(':
                # 如果 opened > 0，說明這不是最外層的 '('
                if opened > 0:
                    res.append(char)
                opened += 1
            else:   # char == ')'
                opened -= 1
                # 如果減完後 opened > 0，說明這不是最外層的 ')'
                if opened > 0:
                    res.append(char)

        return "".join(res)
