
# 40. Combination Sum II
class Solution:
    def combinationSum2(self, candidates: List[int], target: int) : 

        def backtrack(rem, curr, arr, count, results):

            if rem == 0:
                results.append(list(arr))
                return
            elif rem <= 0:
                return

            
            for i in range(curr, len(count)):
                can, freq = count[i]

                if freq <= 0:
                    continue

                arr.append(can)
                count[i] = (can, freq - 1)
                backtrack(rem - can, i, arr, count, results)
                arr.pop()
                count[i] = (can, freq)



        results = []
        c = collections.Counter(candidates)
        # print(c)
        count = [(each, c[each]) for each in c ]

        backtrack(target, 0, [], count, results)
        return results
