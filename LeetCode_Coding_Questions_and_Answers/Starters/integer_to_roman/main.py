class Solution(object):
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        numb = [1, 4, 5, 9, 10, 40, 50, 90,
               100, 400, 500, 900, 1000]
        sym = ["I", "IV", "V", "IX", "X", "XL",
               "L", "XC", "C", "CD", "D", "CM", "M"]
        i = 12
        roman = ""
        while num:
            print(f"Iteration: {i}")
            div = num // numb[i]
            print(f"Div: {div}")
            num %= numb[i]
            print(f"num: {num}")

            while div:
                print(f"Div:{div}")
                roman = roman + sym[i]
                print(f"Roman: {roman}")
                div -= 1
            i -= 1
        return roman
ob = Solution()
print(ob.intToRoman(27))
