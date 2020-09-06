# 42. Trapping Rain Water
class Solution:
    def trap(self, height: List[int]) -> int:
        size = len(height)
        if size<3:
            return 0
        
        total_water = 0
        i,j = 0,size-1
        lmax, rmax = height[0], height[size-1]
        while i<=j :
            lmax, rmax = max(lmax,height[i]), max(rmax,height[j])
            if lmax <= rmax:
                total_water = total_water + lmax-height[i]
                i+=1
            elif rmax<=lmax:
                total_water = total_water + rmax-height[j]
                j-=1
                
        return total_water
        