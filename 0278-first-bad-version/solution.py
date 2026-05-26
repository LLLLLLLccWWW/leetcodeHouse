# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
# def isBadVersion(version):

class Solution(object):
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        left,right = 1,n
        while left < right:
            mid = (left + right) // 2

            if isBadVersion(mid):
                right = mid      # mid是bad，答案在左邊（含mid）
            else:
                left = mid + 1   # mid是good，答案在右邊

        return left  # left==right，就是第一個bad
