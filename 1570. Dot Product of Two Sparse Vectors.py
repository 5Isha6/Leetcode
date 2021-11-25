#1570. Dot Product of Two Sparse Vectors
class SparseVector:
    def __init__(self, nums: List[int]):
        # self.dict = {}
        # for idx,i in enumerate(nums):
        #     if i != 0:
        #         self.dict[idx] = i
        self.nums = nums

    # Return the dotProduct of two sparse vectors
    def dotProduct(self, vec: 'SparseVector') -> int:
        tot = 0
        for i, j in zip(self.nums, vec.nums):
            # for j in vec.nums:
            tot += i * j
        return tot

# Your SparseVector object will be instantiated and called as such:
# v1 = SparseVector(nums1)
# v2 = SparseVector(nums2)
# ans = v1.dotProduct(v2)

