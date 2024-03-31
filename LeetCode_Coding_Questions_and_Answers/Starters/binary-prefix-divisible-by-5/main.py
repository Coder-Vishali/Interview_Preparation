class Solution:
   def prefixesDivBy5(self, A):
      for i in range(1, len(A)):
         A[i] += A[i - 1] * 2 % 5
      return [x % 5 == 0 for x in A]

ob = Solution()
print(ob.prefixesDivBy5([1,0,1]))
