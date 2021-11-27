#53. Maximum Subarray
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        
        curr = max_sum = nums[0]
        
        for i in range(1, len(nums)):
            curr = max(nums[i], curr + nums[i])
            max_sum = max(curr, max_sum)
        return max_sum
            
        
        
        # M2 brute force
        # tot = float("-inf")
        # for i, val in enumerate(nums):
        #     curr = 0
        #     for j  in range(i, len(nums)):
        #         curr += nums[j]
        #         tot = max(tot, curr)
        # return tot
