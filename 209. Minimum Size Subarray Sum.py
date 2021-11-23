#209. Minimum Size Subarray Sum
class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        f = 0
        minimum_w = float('inf')
        
        total_sum = 0
        
        for i in range(len(nums)):
            total_sum += nums[i]
            while total_sum >= target:

                minimum_w = min(i - f + 1, minimum_w)
                total_sum -= nums[f]
                f += 1
        return minimum_w if minimum_w != float('inf') else 0
