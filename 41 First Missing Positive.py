#41 First Missing Positive
class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        N = len(nums)
        for i in range(N):
            if nums[i] <= 0 or nums[i]>N:
                nums[i] = N + 1
        
        for i in nums:
            num = abs(i)
            if num<=N and  nums[num-1] >= 0:
                nums[num-1] *= -1
            
        for i in range(N):
            if nums[i] > 0:
                return i+1
        
        return N+1