class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        # set - Stores all distinct characters
        return len(set(s))

ob=Solution()
print(ob.lengthOfLongestSubstring("abcabcbb"))
