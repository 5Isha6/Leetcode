# 220 Contains Duplicate III.py
# from sortedcontainers import SortedList
class Solution:
    def containsNearbyAlmostDuplicate(self, nums: List[int], k: int, t: int) -> bool:
        size = len(nums)
        # print(nums, set(nums))
        if t == 0 and size == len(set(nums)):
            return False
        
        for idx,j in enumerate(nums):

            for m in range(idx+1,min(idx+1+k,size)) :

                if abs(j - nums[m]) <= t:
                    return True
            
        return False