class Solution:
    def two_sum(self, nums, target):
        prev_map  = {}
        for i, n in enumerate(nums):
            if n in prev_map:
                return [prev_map[n], i]
            
            prev_map[target - n] = i
            
sol = Solution()
# result = sol.two_sum([2,7,11,15], 9)
result = sol.two_sum([3,3], 6)
print(result)