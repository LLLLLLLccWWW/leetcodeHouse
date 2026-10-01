class Solution(object):
    def makeFancyString(self, s):
        """
        :type s: str
        :rtype: str
        """
        res = []

        for char in s:
            # 檢查結果陣列末尾是否已有兩個相同的 char
            if len(res) >= 2 and res[-1] ==char and res[-2] == char:
                continue
            res.append(char)

        return "".join(res)
