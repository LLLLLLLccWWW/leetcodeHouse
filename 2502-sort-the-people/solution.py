class Solution:
    def sortPeople(self, names: list[str], heights: list[int]) -> list[str]:
        # 1. 將 (height, name) 壓縮組合
        # 2. 依照 height 降冪排序
        # 3. 提取 name 輸出
        return [name for _,name in sorted(zip(heights,names),reverse=True)]
