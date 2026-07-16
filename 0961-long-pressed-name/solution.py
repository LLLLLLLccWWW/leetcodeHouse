class Solution(object):
    def isLongPressedName(self, name, typed):
        """
        :type name: str
        :type typed: str
        :rtype: bool
        """
        i,j = 0,0
        len_n,len_t = len(name),len(typed)

        while j < len_t:
            # 情況 1：字元匹配成功
            if i < len_n and name[i] == typed[j]:
                i += 1
                j += 1
                
            # 情況 2：字元不匹配，但 typed[j] 是因為長按造成的重複
            elif j > 0 and typed[j] == typed[j-1]:
                j += 1

            # 情況 3：完全不匹配
            else:
                return False

        return i == len_n
