class Node:
    def __init__(self,key = -1,next = None):
        self.key = key
        self.next = next
class MyHashSet(object):

    def __init__(self):
        self.size = 1999
        self.buckets = [Node() for _ in range(self.size)]

    def _hash(self,key):
        return key % self.size

    def add(self, key):
        """
        :type key: int
        :rtype: None
        """
        if self.contains(key):
            return
        
        idx = self._hash(key)
        curr = self.buckets[idx]

        while curr.next:
            curr = curr.next
        curr.next = Node(key)     

    def remove(self, key):
        """
        :type key: int
        :rtype: None
        """
        idx = self._hash(key)
        curr = self.buckets[idx]

        while curr.next:
            if curr.next.key == key:
                curr.next = curr.next.next
                return
            curr = curr.next

    def contains(self, key):
        """
        :type key: int
        :rtype: bool
        """
        idx = self._hash(key)
        curr = self.buckets[idx].next

        while curr:
            if curr.key == key:
                return True
            curr = curr.next

        return False


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)
