class Solution(object):
    def calPoints(self, operations):
        stack = []

        for op in operations:
            if op == 'C':
                stack.pop()                        # 移除最後一個
            elif op == 'D':
                stack.append(stack[-1] * 2)        # 最後一個的兩倍
            elif op == '+':
                stack.append(stack[-1] + stack[-2]) # 最後兩個相加
            else:
                stack.append(int(op))              # 純數字直接加入

        return sum(stack)
