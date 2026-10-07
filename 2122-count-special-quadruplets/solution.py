from collections import defaultdict
class Solution(object):
    def countQuadruplets(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        ans = 0
        freq = defaultdict(int)
        
        # 從右至左列舉中間點 c
        for c in range(n - 2, 1, -1):
            # 將 c + 1 位置視為 d，更新所有可能的 (nums[d] - nums[c+1]) 到哈希表
            d = c + 1
            for b_idx in range(d + 1, n): # 這裡此處代表後續所有的 d
                pass
            
            # 將目前 c+1 固定的 d 與該位置相減存入 freq
            for d_idx in range(c + 1, n):
                freq[nums[d_idx] - nums[c]] += 1
                
            # 列舉左側所有的 a 與 b
            for a in range(c - 1):
                ans += freq[nums[a] + nums[c - 1]]
                
        return ans
