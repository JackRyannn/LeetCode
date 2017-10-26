# 设计维护一个栈，在python里非常简单
class MinStack(object):
    l = []
    minvalue = 0

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.l = []

    def push(self, x):
        """
        :type x: int
        :rtype: void
        """
        if len(self.l) == 0:
            self.minvalue = x
        self.l.append(x)
        if x < self.minvalue:
            self.minvalue = x

    def pop(self):
        """
        :rtype: void
        """
        i = self.l.pop()
        if i == self.minvalue and len(self.l) > 0:
            self.minvalue = min(self.l)

    def top(self):
        """
        :rtype: int
        """
        return self.l[-1]

    def getMin(self):
        """
        :rtype: int
        """
        return self.minvalue


        # Your MinStack object will be instantiated and called as such:
        # obj = MinStack()
        # obj.push(x)
        # obj.pop()
        # param_3 = obj.top()
        # param_4 = obj.getMin()