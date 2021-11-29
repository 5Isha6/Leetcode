#680. Valid Palindrome II
class Solution:
    def validPalindrome(self, s: str) -> bool:
        
        l, r  = 0, len(s) - 1
        
        def isPalindrome(st):
            return st == st[::-1]
        
        while l < r:
            
            if s[l] != s[r]:
                dele_i = s[l+1:r+1]
                dele_j = s[l:r]
                return isPalindrome(dele_i) or isPalindrome(dele_j)
            
            l += 1
            r -= 1
            
        return True
        
