#269. Alien Dictionary
from collections import defaultdict, Counter, deque
class Solution:
    def alienOrder(self, words: List[str]) -> str:
        adj = defaultdict(set)
        
        indeg = Counter({c : 0 for word in words for c in word})
        
        for f, s in zip(words, words[1:]):
            for c, d in zip(f,s):
                if c!= d:
                    if d not in adj[c]:
                        adj[c].add(d)
                        indeg[d] += 1
                    break
            else:
                if len(f) > len(s):
                    return ""
                
        op = []
        q = deque([i for i in indeg if indeg[i] == 0])
        while q:
            i = q.popleft()
            op.append(i)
            for j in adj[i]:
                indeg[j] -= 1
                if indeg[j] == 0:
                    q.append(j)
        
        if len(op) < len(indeg):
            return ""
        return "".join(op)
        
