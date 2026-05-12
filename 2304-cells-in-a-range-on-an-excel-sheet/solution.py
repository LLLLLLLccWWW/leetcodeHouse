class Solution(object):
    def cellsInRange(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        col1,row1,col2,row2 = s[0],int(s[1]),s[3],int(s[4])

        result = []
        # ord() 把字母轉成數字，chr() 把數字轉回字母
        for col in range(ord(col1),ord(col2) + 1):
            for row in range(row1,row2 + 1):
                result.append(chr(col) + str(row))

        return result
        
