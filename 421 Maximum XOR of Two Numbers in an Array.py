# 421 Maximum XOR of Two Numbers in an Array
class Node:
    def __init__(self):
        self.edges = {}
        
    def add(self,x):
        if x not in self.edges:
            self.edges[x] = Node()
    def get(self, x):
        return self.edges[x]
        
    def has(self,x):
        return x in self.edges
        
class Trie:
    def __init__(self):
        self.root = Node()
        
    def add(self, x):
        current =self.root
        
        for offset in range(31,-1,-1):
            if  (x & (1<<offset )) > 0:
                current.add(1)
                current = current.get(1)
            else:
                current.add(0)
                current=current.get(0)
             
    def getmax(self,x):
        current = self.root
        answer = 0
        for offset in range(31,-1,-1):
            answer*=2
            if (x &(1<< offset)) > 0:
                if current.has(0):
                    current = current.get(0)
                else:
                    current = current.get(1)
                    answer +=1
                    
            else:
                if current.has(1):
                    current = current.get(1)
                    answer +=1
                else:
                    current = current.get(0)
        return x ^ answer
                    
        
        
            
class Solution:
    def findMaximumXOR(self, nums: List[int]) -> int:
        
        trie = Trie()
        best = 0
        trie.add(nums[0])
        for x in nums[1:]:
            best = max(best,trie.getmax(x))
            trie.add(x)
        return best