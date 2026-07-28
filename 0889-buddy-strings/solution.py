class Solution(object):
    def buddyStrings(self, s, goal):
        """
        :type s: str
        :type goal: str
        :rtype: bool
        """
        # 1. 長度不同直接無法透過交換相符
        if len(s) != len(goal):
            return False

        # 2. 兩字串完全相同時，需檢查是否有重複字元供內部交換
        if s == goal:
            return len(set(s)) < len(s)

        # 3. 兩字串不同時，找出所有不符合的位置索引
        diff = []
        for i in range(len(s)):
            if s[i] != goal[i]:
                diff.append(i)
                # 提前剪枝：如果不同位置超過 2 個，不可能只靠一次交換修復
                if len(diff) > 2:
                    return False

        # 必須恰好有 2 個位置不同，且交叉相等
        return len(diff) == 2 and s[diff[0]] == goal[diff[1]] and s[diff[1]] == goal[diff[0]]
