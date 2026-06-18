class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        s.strip()
        return len(s.strip().split()[-1])

obj = Solution()
print(obj.lengthOfLastWord("Hello World"))