class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        # Corner Case (Only one row)
        if numRows == 1:
            print(s)
            return

        # Find length of string
        l = len(s)

        # Create an array of
        # strings for all n rows
        arr = ["" for x in range(l)]

        # Initialize index for
        # array of strings arr[]
        row = 0

        # Traverse through
        # given string
        for i in range(l):

            # append current character
            # to current row
            arr[row] += s[i]

            # If last row is reached,
            # change direction to 'up'
            if row == numRows - 1:
                down = False

            # If 1st row is reached,
            # change direction to 'down'
            elif row == 0:
                down = True

            # If direction is down,
            # increment, else decrement
            if down:
                row += 1
            else:
                row -= 1

        # Print concatenation
        # of all rows
        for i in range(numRows):
            print(arr[i], end = "")

ob = Solution()
ob.convert(s = "PAYPALISHIRING", numRows = 3)
