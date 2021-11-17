#55. Jump Game
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        
        des = len(nums)-1
        for i in range(len(nums)-1,-1,-1):
            if i + nums[i] >= des:
                des = i
        return not des
        
