class Solution(object):
    def canPlaceFlowers(self, flowerbed, n):
        """
        :type flowerbed: List[int]
        :type n: int
        :rtype: bool
        """
        count = 0

        for i in range(len(flowerbed)):
            if flowerbed[i] == 0:
                left = (i == 0) or (flowerbed[i-1] == 0)    # 左邊是空的或是邊界
                right = (i == len(flowerbed)-1) or (flowerbed[i+1] == 0)    # 右邊是空的或是邊界

                if left and right:
                    flowerbed[i] = 1    # 種花
                    count += 1

        return count >= n
