class Node:
    def __init__(self,key=-1,val=-1,next=None):
        self.key = key
        self.val = val
        self.next = next

class MyHashMap(object):

    def __init__(self):
        self.size = 1999
        self.buckets = [Node() for _ in range(self.size)]

    def _hash(self,key):
        return key % self.size

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: None
        """
        idx = self._hash(key)
        curr = self.buckets[idx]

        while curr.next:
            if curr.next.key == key:
                curr.next.val = value
                return
            curr = curr.next

        curr.next = Node(key,value)
        

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        idx = self._hash(key)
        curr = self.buckets[idx].next

        while curr:
            if curr.key == key:
                return curr.val
            curr = curr.next

        return -1
        

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


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)
