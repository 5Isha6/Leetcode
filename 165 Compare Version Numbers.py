#165 Compare Version Numbers
class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        first = [ int(x) for x in version1.split('.')]
        second = [int(x) for x in version2.split('.')]
        
        # print(first,second)
        N = len(second)
        M = len(first)
        # N = if len(first) <= len(second): len(first)
        equal = True
        if M == N:
            for i in range(N):
                if first[i]<second[i]:
                    equal = False
                    return -1
                elif first[i] == second[i] and equal:
                    equal = True
                else:
                    equal = False
                    return 1
                    
            # A+1 if A > B else A-1
            return 1 if not equal else 0

        else:
            N = len(second)
            if len(first) < len(second): N = len(first) 
                
            for i in range(N):
                if first[i]<second[i]:
                    equal = False
                    return -1
                elif first[i] == second[i] and equal:
                    equal = True
                else:
                    equal = False
                    # return 1
            
            if equal:
                if len(first)> len(second):
                    for i in range(N,len(first)):
                        if first[i] != 0:
                            return 1
                else:
                    for i in range(N,len(second)):
                        if second[i] != 0:
                            return -1
            
            # A+1 if A > B else A-1
            return 1 if not equal else 0
        return -1