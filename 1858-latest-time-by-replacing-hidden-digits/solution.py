class Solution(object):
    def maximumTime(self, time):
        """
        :type time: str
        :rtype: str
        """
        res = list(time)

        # 處理小時十位數
        if res[0] == "?":
            res[0] = '2' if res[1] in['?', '0', '1', '2', '3'] else '1'

        # 處理小時個位數
        if res[1] == "?":
            res[1] = '3' if res[0] == '2' else '9' 

        # 處理分鐘十位數
        if res[3] == "?":
            res[3] = '5'

        # 處理分鐘個位數
        if res[4] == "?":
            res[4] = '9'

        return "".join(res)
