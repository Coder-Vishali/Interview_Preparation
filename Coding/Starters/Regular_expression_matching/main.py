import re
class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        pattern = re.compile(rf"{p}")
        return pattern.fullmatch(s)
ob = Solution()
print(ob.isMatch("aa",".*"))
