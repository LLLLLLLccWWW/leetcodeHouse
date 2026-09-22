class Solution(object):
    def countGoodSubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        count = 0

        # 走訪所有長度為 3 的子字串起始點
        for i in range(len(s) - 2):
            a,b,c = s[i],s[i + 1],s[i + 2]
            if a != b and b != c and a != c:
                count += 1

        return count
