# Time:  O(n)
# Space: O(1)

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: List
        :type l2: List
        :rtype: List
        """
        len_l1 = len(l1)
        len_l2 = len(l2)
        carry = 0
        l3 = []
        i = 0
        while i < len_l2 or i <len_l1:
            print(f"Iteration: {i}")
            sum = 0
            if i<len_l1:
                print(f"{l1[i]}+{sum}", end="")
                sum = sum + l1[i]
                print(f"={sum}")
            if i<len_l2:
                print(f"{l2[i]}+{sum}", end="")
                sum = sum + l2[i]
                print(f"={sum}")
            if carry:
                print(f"{sum}+{carry}", end="")
                sum = sum + carry
                print(f"={sum}")
            print(f"Sum: {(sum%10)}")
            print(f"Carry: {sum//10}")
            l3.append((sum%10))
            carry = sum//10
            i+=1
        if carry:
            l3.append(carry)
        return l3

ob =  Solution()
print(f"Output: {ob.addTwoNumbers([9,9,9,9,9,9,9],[9,9,9,9])}")
