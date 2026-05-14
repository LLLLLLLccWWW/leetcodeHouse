class MyQueue(object):

    def __init__(self):
        self.stack_in = []   # 負責push
        self.stack_out = []  # 負責pop/peek

    def push(self, x):
        self.stack_in.append(x)  # 直接加到 stack_in

    def pop(self):
        self._move()             # 確保 stack_out 有東西
        return self.stack_out.pop()

    def peek(self):
        self._move()             # 確保 stack_out 有東西
        return self.stack_out[-1]

    def empty(self):
        return not self.stack_in and not self.stack_out

    def _move(self):
        if not self.stack_out:   # stack_out 空了才移動
            while self.stack_in:
                self.stack_out.append(self.stack_in.pop())
