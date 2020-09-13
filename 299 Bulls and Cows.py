#299 Bulls and Cows
class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        a, b = 0, 0
        N = len(secret)
        secret_use = [False]*N
        guess_use = [False]*N
        
        for index, (answer,g) in enumerate(zip(secret,guess)):
            
            if answer == g:
                secret_use[index] = guess_use[index] = True
                a += 1
        
        for i in range(N):
            if not secret_use[i]:
                for j in range(N):
                    if not guess_use[j] and secret[i] == guess[j]:
                        b += 1
                        secret_use[i] = guess_use[j] = True
                        break
                        
        return f"{a}A{b}B"
            
# class Solution:
    # def getHint(self, secret: str, guess: str) -> str:
        
        # bull=0
        # for i in range(len(secret)):
            # bull += int(secret[i] == guess[i])
        
		# # This loop will take care of "cow" cases
        # cows=0
        # # print(set(secret))
        # for c in set(secret):
            # print(c, secret.count(c),guess.count(c))
            # cows += min(secret.count(c), guess.count(c))
        
        # return f"{bull}A{cows-bull}B"