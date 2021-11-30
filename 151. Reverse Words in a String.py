#151. Reverse Words in a String
class Solution:
    def reverseWords(self, s: str) -> str:
        s = s.strip()
        input_s = s.split(' ')
        stack = []
        for i in input_s:
            if i != '':
                stack.append(i)
        print('st', stack)
        res = ''
        while len(stack) > 0:
            res += stack.pop() + ' '
        return res.rstrip()
