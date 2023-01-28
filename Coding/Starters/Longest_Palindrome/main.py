import collections


class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: int
        """
        longest = ''
        count = dict(collections.Counter(s))
        for each in count:
            if (int(count[each]) % 2)== 0:
                longest = longest + each
        longest =  longest + longest[::-1]
        return longest

ob=Solution()
print(ob.longestPalindrome("cbbd"))
