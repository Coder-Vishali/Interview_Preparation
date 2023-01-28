You are given a binary array nums (0-indexed).

We define xi as the number whose binary representation is the subarray nums[0..i] (from most-significant-bit to least-significant-bit).

For example, if nums = [1,0,1], then x0 = 1, x1 = 2, and x2 = 5.
Return an array of booleans answer where answer[i] is true if xi is divisible by 5.

Example 1:

Input: nums = [0,1,1]
Output: [true,false,false]
Explanation: The input numbers in binary are 0, 01, 011; which are 0, 1, and 3 in base-10.
Only the first number is divisible by 5, so answer[0] is true.

Example 2:

Input: nums = [1,1,1]
Output: [false,false,false]

Note:

1 <= A.length <= 30000
A[i] is 0 or 1
Solutions:

Let's analyze the example 3,

Input: 0 1 1 1 1 1

length 1: 0 decimal value: 0 result: true, 0 is divisible by 5

length 2: 0 1 decimal value: 1 result: false, 1 is not divisible by 5

length 3: 0 1 1 decimal value: 3 result: false

length 4: 0 1 1 1 decimal value: 7 result: false

lenght 5: 0 1 1 1 1 decimal value: 15 result: true

length 6: 0 1 1 1 1 1 decimal value: 31 result: false

Observations here is that whenever we add a new digit number is increase by

                newNumber = oldnumber*2+digit_value
                
If new number is divisible by 5, we add true in our list.

Another interesting fact is any number is divided by 5, they end with 0 or 5. So we can update newNumber by the remainder of

              oldNumber = newNumber%5
              
Why is that? Let's take an example from our above example 3:

newNumber=7
oldNumber=2
next new number will be: 
newNumber = 2*2+1 = 5(answer true)
oldNumber = 5%5=0
next new number will be: 
newNumber = 2*0+1 = 2 (answer false)
