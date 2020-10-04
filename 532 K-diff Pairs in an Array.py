#532 K-diff Pairs in an Array
class Solution:
    def findPairs(self, nums: List[int], k: int) -> int:
        seen = set()
        high = set()
        
        for num in nums:
            if num - k in seen:
                high.add(num)
            
            if num + k in seen:
                high.add(num+k)
                
            seen.add(num)
        return len(high)