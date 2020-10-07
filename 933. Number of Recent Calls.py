#933. Number of Recent Calls
from collections import deque
class RecentCounter:
    
    def __init__(self):
        # self.c = 0
        # self.store = []
        self.s = deque()
        # return None
    # global c 
    def ping(self, t: int) -> int:
        # if  t >= t - 3000:
        self.s.append(t)
        while self.s[0] < t-3000:
            self.s.popleft()
        return len(self.s)
        