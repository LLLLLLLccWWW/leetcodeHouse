class Solution(object):
    def flipAndInvertImage(self, image):
        """
        :type image: List[List[int]]
        :rtype: List[List[int]]
        """
        n = len(image)
        for row in image:
            left,right = 0,n - 1
            while left <= right:
                # 當兩端元素相同時，翻轉+反轉後數值才會改變
                if row[left] == row[right]:
                    row[left] = row[left] ^ 1
                    row[right] = row[left]  # 若 left == right，這步也不會影響結果
                left += 1
                right -= 1
        return image
