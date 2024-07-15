class Solution(object):
    def maximumGain(self, s, x, y):
        def remove(s, value, first, second):
            stack = []
            result = 0
            for char in s:
                if stack and stack[-1] == first and char == second:
                    stack.pop()
                    result += value
                else:
                    stack.append(char)
            return ''.join(stack), result

        if x > y:
            s, score1 = remove(s, x, 'a', 'b')
            s, score2 = remove(s, y, 'b', 'a')
        else:
            s, score1 = remove(s, y, 'b', 'a')
            s, score2 = remove(s, x, 'a', 'b')

        return score1 + score2

solution = Solution()
s = "cdbcbbaaabab"
x = 4
y = 5
print(solution.maximumGain(s, x, y))
