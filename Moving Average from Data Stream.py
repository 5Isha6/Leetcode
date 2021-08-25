#Moving Average from Data Stream
class MovingAverage:
    

    def __init__(self, size: int):
        """
        Initialize your data structure here.
        """
        self.size = size
        self.ip = []
        

    def next(self, val: int) -> float:
        self.ip.append(val)
        dist = min(self.size, len(self.ip))
        #print('dist',dist, sum(self.ip[:-dist]))
        ma = sum(self.ip[-dist:])/dist
        #print('ma',ma)
        return ma


# Your MovingAverage object will be instantiated and called as such:
# obj = MovingAverage(size)
# param_1 = obj.next(val)
