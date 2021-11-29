#953. Verifying an Alien Dictionary
class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        char_index = defaultdict(int)
        
        for ind, val in enumerate(order):
            char_index[val] = ind
        
        for i in range(len(words) - 1):
            
            for j in range(len(words[i])):
                if j >= len(words[i+1]):
                    return False
                
                if words[i][j] != words[i+1][j]:
                    if char_index[words[i][j]] > char_index[words[i+1][j]]:
                        return False
                    break
        return True
        
        
