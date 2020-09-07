#290 Word Pattern

class Solution:
    def wordPattern(self, pattern: str, str: str) -> bool:
        lookup = {}
        rev_lookup = {}
        if len(pattern) != len(str.split()):
            return False
        for char, word in zip(pattern,str.split()):
            # print(char,word)
            if char in lookup:
                # print( lookup[char] , word)
                if lookup[char] != word:
                    return False
            else:
                lookup[char] = word

        
            if word in rev_lookup:
                if rev_lookup[word] != char:
                    return False
            else:
                rev_lookup[word] = char
        return True 
    