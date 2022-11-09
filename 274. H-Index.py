class Solution:
    def hIndex(self, citations: List[int]) -> int:

        
        cnt = 0
        for i, j in  enumerate(sorted(citations, reverse = True)):
            if i < j:
                cnt += 1
        return cnt
        # return sum( i < j for i, j in enumerate(sorted(citations, reverse = True)) )
