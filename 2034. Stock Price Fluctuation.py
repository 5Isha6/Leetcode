# 2034. Stock Price Fluctuation 
import heapq
class StockPrice:

    def __init__(self):
        self.dict = {}
        self.currtime = -math.inf
        self.minheap = []
        self.maxheap = []

    def update(self, timestamp: int, price: int) -> None:
        self.dict[timestamp] = price
        
        self.currtime = max(timestamp, self.currtime)
        
        heappush(self.maxheap, (-price, timestamp))
        heappush(self.minheap, (price, timestamp))
        

    def current(self) -> int:
        return self.dict[self.currtime]
        

    def maximum(self) -> int:
        p, t = heappop(self.maxheap)

        while -p != self.dict[t]:
            p, t = heappop(self.maxheap)

        heappush(self.maxheap, (-p,t))

        return -p

    def minimum(self) -> int:
        p, t = heappop(self.minheap)

        while p != self.dict[t]:
            p, t = heappop(self.minheap)

        heappush(self.minheap, (p,t))
        return p
        


# Your StockPrice object will be instantiated and called as such:
# obj = StockPrice()
# obj.update(timestamp,price)
# param_2 = obj.current()
# param_3 = obj.maximum()
# param_4 = obj.minimum()
