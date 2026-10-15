from collections import Counter
class Solution(object):
    def findEvenNumbers(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        digits_count = Counter(digits)
        ans = []

        # 直接列舉所有合法的 3 位偶數 (100 ~ 998, 步長 2)
        for num in range(100,1000,2):
            d1 = num // 100     # 百位
            d2 = (num // 10) % 10   # 十位
            d3 = num % 10           # 個位

            num_count = Counter([d1,d2,d3])

            # 檢查 digits 是否能提供組成該數字所需的各數位數量
            if all(digits_count[d] >= count for d,count in num_count.items()):
                ans.append(num)

        return ans
