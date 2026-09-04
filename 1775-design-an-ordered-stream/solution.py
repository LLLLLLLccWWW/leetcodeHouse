class OrderedStream(object):

    def __init__(self, n):
        """
        :type n: int
        """
        self.storage = [None] * (n + 1)
        self.ptr = 1
        

    def insert(self, idKey, value):
        """
        :type idKey: int
        :type value: str
        :rtype: List[str]
        """
        self.storage[idKey] = value
        result = []

        while self.ptr < len(self.storage) and self.storage[self.ptr] is not None:
            result.append(self.storage[self.ptr])
            self.ptr += 1
        return result

        


# Your OrderedStream object will be instantiated and called as such:
# obj = OrderedStream(n)
# param_1 = obj.insert(idKey,value)
