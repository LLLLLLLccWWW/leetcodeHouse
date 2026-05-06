class Solution(object):
    def isValid(self, s):
        stack = []
        mapping = {
            ')': '(',
            '}': '{',
            ']': '['
        }

        for char in s:
            if char in mapping:     # 是右括號
                if not stack or stack[-1] != mapping[char]:  
                    return False    # stack 為空或頂端不對應
                stack.pop()        # 對應成功，把左括號移出
            else:                 # 是左括號
                stack.append(char)  # 把左括號放入 stack
        
        return len(stack) == 0  # 最後 stack 應該是空的

        
