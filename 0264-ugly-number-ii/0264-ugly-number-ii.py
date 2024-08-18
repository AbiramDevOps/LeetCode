class Solution(object):
    def nthUglyNumber(self, n):
        heap = [1]
        seen = set(heap)  # To avoid duplicate numbers
        result = []
        
        # Generate numbers
        while len(result) < n:
            smallest = heapq.heappop(heap)
            result.append(smallest)
            
            # Generate new numbers by multiplying the smallest number by 2, 3, and 5
            for factor in [2, 3, 5]:
                new_number = smallest * factor
                if new_number not in seen:
                    seen.add(new_number)
                    heapq.heappush(heap, new_number)
        
        return result[-1]

solution = Solution()
print(solution.nthUglyNumber(11))