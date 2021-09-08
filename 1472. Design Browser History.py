# 1472. Design Browser History
class BrowserHistory:

    def __init__(self, homepage: str):
        self.urls = [homepage]
        self.curr = 0

    def visit(self, url: str) -> None:
        
        self.urls = self.urls[:self.curr + 1]
        self.urls.append(url)
        
        self.curr = self.urls.index(url)
        

    def back(self, steps: int) -> str:
        
        te = self.urls[max(0,self.curr - (steps))]
        self.curr -= steps 
        self.curr = max(self.curr,0)
        
        return  te #, len(self.urls)-self.curr)]
    
        

    def forward(self, steps: int) -> str:
        
        t = self.urls[min( (self.curr + steps), len(self.urls)-1)] 
        self.curr += steps
        self.curr = min(self.curr,(len(self.urls)-1))
        return t
                         


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)
