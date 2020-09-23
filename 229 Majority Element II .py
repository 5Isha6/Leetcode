# 229 Majority Element II 
class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        if not nums:
            return []
        
        c1, c2 = 0, 0
        can1, can2 = None, None
        
        for i in nums:
            
            if i == can1:
                c1 += 1
            elif i == can2:
                c2 += 1
            elif c1 == 0:
                can1 = i
                c1 += 1
            elif c2 == 0:
                can2 = i
                c2 += 1
                
            else:
                c1 -= 1
                c2 -= 1
        
        return [x for x in (can1, can2) if nums.count(x) > len(nums)//3]
            
        