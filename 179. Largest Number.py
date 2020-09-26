# 179. Largest Number
class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        snums = list(map(str,nums))
        def comp(a, b):
            if a+b > b+a:
                return -1
            elif a+b < b+a:
                return 1
            else:
                return 0
            
        return str(int("".join(sorted(snums,key=cmp_to_key(comp)))))
        
        