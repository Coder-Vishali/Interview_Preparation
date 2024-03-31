class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        prefix = ""

        for chars in zip(*strs):
            print(f"chars: {chars}")
            if all(c == chars[0] for c in chars):
                prefix += chars[0]
            else:
                return prefix

        return prefix
ob = Solution()
print(ob.longestCommonPrefix(["flower","flow","flight"]))
