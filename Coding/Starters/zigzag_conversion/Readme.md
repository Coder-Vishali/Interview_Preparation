The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this: (you may want to display this pattern in a fixed font for better legibility)

P   A   H   N

A P L S I I G

Y   I   R

And then read line by line: "PAHNAPLSIIGYIR"

Write the code that will take a string and make this conversion given a number of rows:

string convert(string s, int numRows);
 

Example 1:

Input: s = "PAYPALISHIRING", numRows = 3

Output: "PAHNAPLSIIGYIR"

Example 2:

Input: s = "PAYPALISHIRING", numRows = 4

Output: "PINALSIGYAHRPI"

Explanation:

P     I    N

A   L S  I G

Y A   H R

P     I

Example 3:

Input: s = "A", numRows = 1

Output: "A"
 

Constraints:

1 <= s.length <= 1000

s consists of English letters (lower-case and upper-case), ',' and '.'.

1 <= numRows <= 1000

Approach: The given problem is an implementation based problem that can be solved by following the below steps

Create an array of N strings, arr[N].

Initialize direction as “down” and row as 0. The direction indicates whether the current pointer is moving up or down in rows.

Traverse the input string, do the following for every character.

Append the current character to the string representing the current row.

If row number is N – 1, then change direction to ‘up’

If row number is 0, then change direction to ‘down’

If direction is ‘down’, do row++.  Else do row–.

One by one print all strings of arr[].
