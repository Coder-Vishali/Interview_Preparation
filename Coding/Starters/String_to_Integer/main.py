class Solution:
    def myAtoi(self, s: str) -> int:
        s = s.strip()
        new_s = ""
        neg = 0
        dig = False
        for char in s:
            if char.isdigit():
                dig = True
                new_s = new_s + char
            elif char=='+':
                neg = 0
            elif char == "-":
                neg = 1
        num = int(new_s)
        if dig == False:
            num = 0
        if neg:
            num*=-1
        if num > (2**-31) and neg:
            num = 2**-31
            return num
        elif num > ((2**31) -1):
            num = (2**31) -1
            return num
        else:
            return num
ob = Solution()
print(ob.myAtoi("words and 00987"))
