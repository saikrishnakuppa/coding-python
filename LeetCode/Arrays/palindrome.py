class Solution:
    def isPalindrome(self, s: str) -> bool:
        new = ''
        for a in s:
            if a.isalpha() or a.isdigit():
                new += a.lower()
        print(new)
        print(new[::-1])
        return (new == new[::-1])
sol = Solution()
print(sol.isPalindrome(" "))