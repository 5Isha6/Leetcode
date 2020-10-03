#713. Subarray Product Less Than K
class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        tot = 0
        N = len(nums)
        run = 1
        left = 0
        
        for right in range(N):
            run *= nums[right]
            while left<right and run>=k:
                run //= nums[left]
                left += 1
            if run<k:                
                tot += right-left +1
        
        return tot