class Solution(object):
    def removeDuplicates(self, s):
        """
        :type s: str
        :rtype: str
        """
        stack = []

        for c in s:
            if stack and stack[-1] == c:
                stack.pop() # 相同就消掉
            else:
                stack.append(c) # 不同就加入
        
        return ''.join(stack)
