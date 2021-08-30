# 547 Friend circles
from collections import defaultdict, deque
class Solution:
    """
    @param M: a matrix
    @return: the total number of friend circles among all the students
    """
    def findCircleNum(self, M):
        # Write your code here
        n = len(M)
        visit = defaultdict(lambda: False)
        
        ans = 0
        for i in range(n):
          q = deque()
          if not visit[i]:
            ans += 1
            q.append(i)
            visit[i] = True

            while len(q) !=0 :
              curr = q.popleft()
              
              for j in range(n):
                if M[curr][j] == 1 and not visit[j] :
                  q.append(j)
                  visit[j] = True
              
        #print('A',ans)
        return ans

