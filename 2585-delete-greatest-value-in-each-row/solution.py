class Solution:
    def deleteGreatestValue(self, grid: list[list[int]]) -> int:
        # 1. 將每一行升序排序
        for row in grid:
            row.sort()

        # 2. 利用 zip(*grid) 進行矩陣轉置，取每一欄（Column）的最大值並累加
        return sum(max(col) for col in zip(*grid))
