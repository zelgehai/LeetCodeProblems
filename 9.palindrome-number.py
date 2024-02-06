#
# @lc app=leetcode id=9 lang=python
#
# [9] Palindrome Number
#

# @lc code=start
class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        reversed_number = 0
        number = x

        while x>0:
            digit = x%10
            x = x//10
            reversed_number = reversed_number*10+digit
            print(reversed_number)
        return reversed_number == number
        
# @lc code=end

