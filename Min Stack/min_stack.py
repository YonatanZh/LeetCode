import heapq

class MinStack(object):
    def __init__(self):
        self._heap = []
        self._q = []

    def push(self, val):
        """
        :type val: int
        :rtype: None
        """
        self._q.append(val)
        heapq.heappush(self._heap, val)

    def pop(self):
        """
        :rtype: None
        """
        if self._heap[0] == self.top():
            heapq.heappop(self._heap)
            self._q.pop()
        else:
            removed = self._q.pop()
            self._heap.remove(removed)
            heapq.heapify(self._heap)

    def top(self):
        """
        :rtype: int
        """
        return self._q[-1]

    def getMin(self):
        """
        :rtype: int
        """
        return self._heap[0]
