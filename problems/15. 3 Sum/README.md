[problem link](https://leetcode.com/problems/3sum/description/)

# Approach

- We need to sort the nums.
- Then, run two pointer approach for rest of the nums while running a for loop for first value.
- You should skip elements next to current elements. So that we don't take duplicate combinations.
- Final thing to remember, Try to use Hash set for unique combinations.

# Complexity

- Time complexity:
  O(n\*\*2)

- Space complexity:
  O(n)

# Code

```python []
class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = set()
        nums.sort()
        for i in range(len(nums)-2):

            l, r = i+1, len(nums)-1
            while l < r:
                s = nums[i] + nums[l] + nums[r]
                if s < 0:
                    l +=1
                elif s > 0:
                    r -= 1
                else:
                    res.add((nums[i], nums[l], nums[r]))
                    while l < r and nums[l] == nums[l+1]:
                        l += 1
                    while l < r and nums[r] == nums[r-1]:
                        r -= 1
                    l += 1; r -= 1
        return res

```
