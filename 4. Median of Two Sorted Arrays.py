# 4. Median of Two Sorted Arrays
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        m = len(nums1)
        n = len(nums2)
        #l = min(m,n)
        res = []
        i, j = 0, 0
        
        #for i in range(len(l)):
        while i < m and j < n:
            if nums1[i] < nums2[j]:
                res.append(nums1[i])
                i += 1
            elif nums1[i] > nums2[j]:
                res.append(nums2[j])
                j += 1
            else:
                res.append(nums1[i])
                res.append(nums2[j])
                i += 1
                j += 1
        
        if i == m:
            res.extend(nums2[j:])
        else:
            res.extend(nums1[i:])
        print(res,m, n , ((m+n)/2))
        l = (m+n)//2
        op = 0
        if (m+n)%2 == 0:
            op = (res[l-1] + res[l])/2
        else:
            op = res[((m+n)//2)]
        return op
