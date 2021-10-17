# 843. Guess the Word
# """
# This is Master's API interface.
# You should not implement it, or speculate about its implementation
# """
# class Master:
#     def guess(self, word: str) -> int:

class Solution:
    def findSecretWord(self, wordlist: List[str], master: 'Master') -> None:
        
        def match(s1,s2):
            return sum(i == j for i, j  in zip(s1, s2))
        
        n = 0
        print(wordlist)
        while n < 6:
            
            cnt = [collections.Counter(w[i] for w in wordlist) for i in range(6)]
            guess = max(wordlist, key=lambda w: sum(cnt[i][c] for i,c in enumerate(w)))
            n = master.guess(guess)
            wordlist = [w for w in wordlist if match(w, guess) == n]
