# 3. Longest Substring Without Repeating Characters
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        w_st = 0
        char_index = defaultdict(int)
        max_len = 0
        for w_ed in range(len(s)):
            
            last_char = s[w_ed]
            
            
            if last_char in char_index:
                
                w_st = max(w_st, char_index[last_char])
                
            char_index[last_char] = w_ed + 1
            max_len = max(max_len, w_ed - w_st + 1)
            
        return max_len
                
        
        
        
        # M2
        w_st = 0
        char_freq = defaultdict(int)
        max_len = 0
        for w_ed in range(len(s)):
            
            last_char = s[w_ed]
            char_freq[last_char] += 1
            # print(char_freq)
            
            while char_freq[last_char] > 1:
                
                first_char = s[w_st]
                char_freq[first_char] -= 1
                w_st += 1
                
            max_len = max(max_len, w_ed - w_st + 1)
        return max_len
                
