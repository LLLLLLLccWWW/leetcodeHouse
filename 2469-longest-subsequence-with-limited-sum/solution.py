from bisect import bisect_right
from itertools import accumulate
class Solution:
    def answerQueries(self, nums: list[int], queries: list[int]) -> list[int]:
        # 1. 貪婪策略：從小到大排序
        nums.sort()

        # 2. 原地生成前綴和陣列
        prefix = list(accumulate(nums))

        # 3. 對每個 query 進行二分搜尋
        # bisect_right 回傳大於 target 的第一個位置，剛好等於符合條件的最大個數
        return [bisect_right(prefix,q) for q in queries]
