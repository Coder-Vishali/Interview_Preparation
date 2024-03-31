# Problem statement
# Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
#
# You may assume that each input would have exactly one solution, and you may not use the same element twice.
#
# You can return the answer in any order.
#
# Input: nums = [2,7,11,15], target = 9
# Output: [0,1]
# Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].

#  Brute Force Method
# In this approach I will iterate the array using two loops to find if the sum is equal to the target.

# A brute force algorithm solves a problem through exhaustion:
# it goes through all possible choices until a solution is found.
# The time complexity of a brute force algorithm is often proportional
# to the input size. Brute force algorithms are simple and consistent,
# but very slow.

# creating an empty list
nums = []

# number of elements as input
n = int(input("Enter number of elements in num list : "))
target = int(input("Enter target value : "))

# iterating till the range
for i in range(0, n):
    ele = int(input("Enter the values of the num list:"))
    nums.append(ele)  # adding the element

print(f"\nNum: {nums}")
print(f"Target: {target}")

# creating an empty result list to store output
result = []

for i in range(0, len(nums)):
    for j in range(i+1, len(nums)):
        if (nums[i]+nums[j]==target):
            result.append(i)
            result.append(j)
            print(f"Result of brute force algorithms : {result}")

if len(result)==0:
    print("No match found!")

# Time Complexity - O(n*n)
# Space Complexity - O(1)


# Using Hashmap

# In this approach I will use hashmap and a list to return
# the index of the elements if the target is found by addition
# of two elements.

# Time Complexity - O(n) because I will traverse the array
# only once and Hashmap has a time complexity of O(1) for insertion.
# Space Complexity - O(1)

result = []
for i in range(0,len(nums)):
    val = target-nums[i]
    if val in nums and nums.index(val)!=i:
        result.append(nums.index(val))
        result.append(i)
        print(f"Result of hash map: {result}")
        break
