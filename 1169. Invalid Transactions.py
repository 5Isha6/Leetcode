#1169. Invalid Transactions
class Solution:
    
     def invalidTransactions(self, transactions: List[str]) -> List[str]:
        res = []
        no = len(transactions)
        visit = [1]*no
        for i in range(no):
            n, t, a, c = transactions[i].split(',')
            t = int(t)
            if int(a) > 1000:
                
                visit[i] = 0
            for j in range(i+1,no):
                nj, tj, aj, cj = transactions[j].split(',')
                tj = int(tj)
                if n == nj and abs(tj-t) <= 60 and cj != c:
                    visit[i] = 0
                    visit[j] = 0
                
           
        print(visit)    
        for i in range(no):
            if not visit[i]:
                res.append(transactions[i])
        
        return res
    
       
