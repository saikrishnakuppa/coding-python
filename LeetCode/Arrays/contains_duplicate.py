class Solution:
    def contains_duplicate(self, nums): 
        hashset = set()
        for n in nums:
            print(hashset)
            if n in hashset:
                return True
            hashset.add(n)
        return False
sol = Solution()
result = sol.contains_duplicate([1,2,3,1])
if result:
    print("YES, duplicates found.")
else:
    print("NO duplicates found.")