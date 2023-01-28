class Solution:
    def isPalindrome(self, x: int) -> bool:
        original = x
        if x < 0:
            return False
        reversed_num = 0
        while x != 0:
            digit = x % 10
            reversed_num = reversed_num * 10 + digit
            x //= 10
        if original == reversed_num:
            return True
        else:
            return False

ob = Solution()
print(ob.isPalindrome(-121))
