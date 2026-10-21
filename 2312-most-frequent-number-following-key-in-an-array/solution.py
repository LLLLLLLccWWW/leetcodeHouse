from collections import Counter
class Solution(object):
    def mostFrequent(self, nums, key):
        """
        :type nums: List[int]
        :type key: int
        :rtype: int
        """
        # 收集所有緊跟在 key 後面的元素並計算出現頻率
        counts = Counter(nums[i + 1] for i in range(len(nums) - 1) if nums[i] == key)

        # 回傳出現次數最多的數字
        return counts.most_common(1)[0][0]
