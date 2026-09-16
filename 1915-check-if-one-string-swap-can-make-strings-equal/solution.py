class Solution(object):
    def areAlmostEqual(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
        # 紀錄字元不相等的索引位置
        diff = []

        for i in range(len(s1)):
            if s1[i] != s2[i]:
                diff.append(i)
                if len(diff) > 2:
                    return False

        # 不相等的位置數量為 0 (完全相同)
        if len(diff) == 0:
            return True

        # 不相等的位置數量為 2，且對角字元相等
        if len(diff) == 2:
            i,j = diff
            return s1[i] == s2[j] and s1[j] == s2[i]

        return False
