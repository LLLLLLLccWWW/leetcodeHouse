class Solution(object):
    def arrangeCoins(self, n):
        """
        :type n: int
        :rtype: int
        """
        left,right = 0,n

        while left <= right:
            mid = (left + right) // 2
            coins = mid * (mid + 1) // 2    # 前mid行需要的硬幣數

            if coins == n:
                return mid          # 剛好用完
            elif coins < n:
                left = mid + 1      # 還可以更多行
            else:
                right = mid - 1     # 太多了，減少行數
                
        return right
