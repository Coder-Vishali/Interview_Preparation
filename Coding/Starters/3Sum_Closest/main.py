class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        result, min_diff = 0, float("inf")
        nums.sort()
        for i in reversed(range(2, len(nums))):
            if i+1 < len(nums) and nums[i] == nums[i+1]:
                continue
            left, right = 0, i-1
            while left < right:
                total = nums[left]+nums[right]+nums[i]
                if total < target:
                    left += 1
                elif total > target:
                    right -= 1
                else:
                    return target
                if abs(total-target) < min_diff:
                    min_diff = abs(total-target)
                    result = total
        return result

ob=Solution()
print(ob.threeSumClosest([-1,2,1,-4],1))
