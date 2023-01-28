class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        num3 = nums1 + nums2
        num3.sort()
        n = len(num3)
        if ((n%2)!=0):
            return num3[int(n/2)]
        else:
            return (num3[int(n/2)-1] + num3[int(n/2 + 1)-1])/2

ob=Solution()
print(ob.findMedianSortedArrays([1,2],[3,4]))
