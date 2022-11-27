#752. Open the Lock
class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        
               
        def neighbours(node):
            
            for i in range(len(node)):
                x = int(node[i])
                for d in (-1, 1):
                    new_i = (x + d)%10
                    yield node[:i] + str(new_i) + node[i+1:]
        
        
        
        
        q = deque([("0000", 0)])
        visit = set(("0000"))
        
        while q:
            
            newnode, depth = q.popleft()
            if newnode == target: return depth
            if newnode in deadends : continue
            
            for i in neighbours(newnode):
                if i not in visit:
                    q.append((i, depth + 1))
                    visit.add((i))
            
            
            
        return -1
