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
            
# Generic K https://leetcode.com/problems/majority-element-ii/discuss/617643/Python-Scalable-General-NO-MATH-O(n)-Time-O(1)-Space-90-faster
# if element is found in our map of candidates, we +1 its value (count)

# if there is room to add a new candidate (candidates number < k ), we add it

# if our space is full and no room to add any new candidate we -1 all candidates

# we want to remove the candidates that have reached zero and keep only the candidates who are >= 1, therefore we create a temp_dict and then we make the old dict (candidates) = temp_dict

# At the end in linear time we go through the original array to count the number of times our suggest candidates appeared and check if they are > n//3			
 # class Solution:
  	# def majorityElement(self, nums: List[int]) -> List[int]:
  		# candidates = {}
  		# k = 3
  		# for num in nums:
  			# if num in candidates:
  				# candidates[num] += 1
  			# elif len(candidates) < k:
  				# candidates[num] = 1
  			# else:
  				# temp={}
  				# for c in candidates:
  					# candidates[c]-=1
  					# if candidates[c] >= 1:
  						# temp[c] = candidates[c]
  				# candidates = temp
  		# out = [k for k in candidates if nums.count(k) > len(nums) // 3]          
  		# return out
        