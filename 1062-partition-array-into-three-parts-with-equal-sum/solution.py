class Solution(object):
    def canThreePartsEqualSum(self, arr):
        """
        :type arr: List[int]
        :rtype: bool
        """
        total_sum = sum(arr)

        # 若總和不能被 3 整除，絕對無法分成三等份
        if total_sum % 3 != 0:
            return False

        target = total_sum // 3
        count = 0
        cur_sum = 0

        # 遍歷陣列，計算段數
        for num in arr:
            cur_sum += num
            if cur_sum == target:
                count += 1
                cur_sum = 0     # 歸零重新計算下一段
                
        # 只要找到了至少 3 段（多的可能是 target == 0 時中間夾雜的多餘 0 段），即代表可以分成三等份
        return count >= 3
