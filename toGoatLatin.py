class Solution:
    def toGoatLatin(self, S: str) -> str:
        
        result = S.split(' ')
        print(result)
        for word in range(len(result)):
            
            
                
            if result[word][0].lower() not in ['a', 'e', 'i', 'o', 'u']:
                result[word] = result[word][1:] + result[word][0]
                
            result[word] += "ma"
            addition = "a"
            for j in range(word):
                addition += "a"

            result[word] += addition

        final = ' '.join(result)
        return final