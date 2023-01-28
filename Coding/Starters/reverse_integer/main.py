class Solution:
    def reverse(self, x: int) -> int:
        rev = 0
        neg = False
        if x < 0:
            neg = True
            x = x * -1
        while (x > 0):
            a = x % 10
            rev = rev * 10 + a
            x = x // 10
        if rev > 2**31:
            rev = 0
        if neg:
            rev = rev * -1
        return rev

ob = Solution()
print(ob.reverse(4562))
