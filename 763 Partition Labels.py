# 763 Partition Labels
class Solution:
    def partitionLabels(self, S: str) -> List[int]:
        
        size = len(S)
        if size == 0 or S == None: return []
        result = []
        i = 0
       
        while i < size:
            maxi = S.rfind(S[i])
            
            j = i+1
            while j <= maxi:
                maxj = S.rfind(S[j])
                
                if maxj>maxi:
                    maxi = maxj
                j+=1
            
            result.append(maxi-i+1)
            i = maxi
            i+=1
        return result
        