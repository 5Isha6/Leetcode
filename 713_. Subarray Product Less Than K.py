# 713. Subarray Product Less Than K
class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        
        st, prod = 0, 1
        cnt = 0
        for i in range(len(nums)):
            
            prod *= nums[i]
            
            while prod >= k and st <= i:
                
                prod /= nums[st]
                st += 1
            
            cnt += i - st + 1
        return cnt
