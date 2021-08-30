#547 Friend Circles DFS
from collections import defaultdict, deque
class Solution:
    """
    @param M: a matrix
    @return: the total number of friend circles among all the students

    """
    def findCircleNum(self, M):
      visit = defaultdict(lambda:False)
      n = len(M)
      ans = 0
      for i in range(n):
        if not visit[i]:
          visit[i] = True
          ans += 1
          self.dfs(i,M,visit)
      print('A', ans)
      return ans
        

    def dfs(self,i,M, visit):
      for j in range(len(M)):
        if not visit[j] and M[i][j] == 1:
          visit[j] = True
          self.dfs(j,M,visit)
