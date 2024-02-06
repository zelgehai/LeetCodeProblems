#
# @lc app=leetcode id=1 lang=python
#
# [1] Two Sum
#

# @lc code=start
""" Slow Method: (First attempt) Brute Force (O(n^2))
 for i in range (len(nums)):
            for j in range(i+1, len(nums)):
                print(i,j)
                if (nums[i] + nums[j] == target):
                    print("Success!" , nums[i] , "+" , nums[j] , "= " , target)
                    return[i,j]
"""

"""
#Single pass Hash Map: beats 88%
 seen = {} #Value = index
        for idx, n in enumerate(nums):
            diff = target - n
            if diff in seen:
                return [seen[diff],idx]
            seen[n] = idx

""" 
#possible better approach is: two-pointer approach 
#see: https://www.nileshblog.tech/leet-code-two-sum-problem-solution-java-cpp-javascript-python/
class Solution(object):
    def twoSum(self, nums, target):
        #zel's code
        seen = {} #Value = index
        for idx, n in enumerate(nums):
            diff = target - n
            if diff in seen:
                return [seen[diff],idx]
            seen[n] = idx

        
# @lc code=end

