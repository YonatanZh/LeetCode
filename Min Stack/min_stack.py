class MinStack(object):
    def __init__(self):
        self._q = []
        self._min = None

    def push(self, val):
        """
        :type val: int
        :rtype: None
        """
        self._q.append(val)
        if self._min is None:
            self._min = val
        elif self._min > val:
            self._min = val

    def pop(self):
        """
        :rtype: None
        """
        removed = self.top()
        self._q.pop()
        if self._q == []:
            self._min = None
        elif self._min == removed:
            self._min = min(self._q)

    def top(self):
        """
        :rtype: int
        """
        return self._q[-1]

    def getMin(self):
        """
        :rtype: int
        """
        return self._min
