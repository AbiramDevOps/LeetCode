class Solution(object):
    def minOperations(self, nums, k):
        match_list = list(range(1, k+1))

        result = []

        for x in reversed(nums): # [1,3,5,2,3]
            result.append(x)
            if x in match_list:
                match_list.remove(x)
                if match_list == []:
                    break

        return len(list(reversed(result)))

nums = [3,2,5,3,1]
k = 3
solution = Solution()
print(solution.minOperations(nums, k)) #output: [2,5,3,1]
