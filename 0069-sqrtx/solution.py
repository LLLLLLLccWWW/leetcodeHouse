class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x == 0:
            return 0
        
        left = 1
        right = x
        ans = 0

        while left <= right:
            mid = (left + right) // 2

            if mid * mid == x:
                return mid   # 剛好整除，直接回傳
            elif mid * mid < x:
                ans = mid   # 記錄當前答案，往右找更大的
                left = mid + 1
            else:
                right = mid - 1  # 太大，往左找
        return ans
