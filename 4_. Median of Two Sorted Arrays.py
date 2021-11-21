#4. Median of Two Sorted Arrays
class Solution:


    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        
        
        def helper(num1,num2,k):
            
            if not num1:
                return num2[k]
            if not num2:
                return num1[k]
            
            a, b = len(num1)//2, len(num2)//2
            m1, m2 = num1[a], num2[b]
            if a + b < k:
                if m1 > m2:
                    return helper(num1,num2[b+1:], k - b - 1)
                else:
                    return helper(num1[a+1:],num2, k - a - 1)
            
            else:
                if m1 > m2:
                    return helper(num1[:a],num2, k )
                    
                else:
                    
                    return helper(num1,num2[:b], k )
        
        l = len(nums1) + len(nums2)
        
        if l % 2 == 0:
            
            return (helper(nums1,nums2,l//2) + helper(nums1,nums2,l//2 - 1))  /2
        else:
            return helper(nums1, nums2, l//2)
        
        
        
        
        
