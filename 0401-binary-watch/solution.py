class Solution(object):
    def readBinaryWatch(self, turnedOn):
        """
        :type turnedOn: int
        :rtype: List[str]
        """
        result = []
        for h in range(12): # 小時 0~11
            for m in range(60): # 分鐘 0~59
                 # bin(n) 把數字轉成二進位字串，count('1') 數1的個數
                if bin(h).count('1') + bin(m).count('1') == turnedOn:
                    result.append("%d:%02d" % (h,m))
        return result
        
