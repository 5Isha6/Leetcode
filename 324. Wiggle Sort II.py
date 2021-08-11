#324. Wiggle Sort II
import copy
class Solution:
    def wiggleSort(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        nums.sort()
        n = len(nums)
        i = int((n-1)/2)
        j = n - 1
        #print(n,i,j)
        alter = 0
        res = []
        for k in range(n):
            #print(alter)
            if alter == 0:
                res.append(nums[i])
                i -= 1
            else:
                res.append(nums[j])
                j -= 1
            #print('i,j,', i, j, res)
            alter = 1 - alter
        nums[:] = res[:]
        
