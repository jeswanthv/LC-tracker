[problem link](https://leetcode.com/problems/container-with-most-water/description/)

# Intuition

We need to find maximum area between two lines in the graph.

# Approach

- We can create a vairable which will store the largest area and two pointers starting from start and end.
- Now, Lets' change the pointer if the height is lesser than the other pointer's height(accordingly) so that we can cover large portion of the area.
- Finally, return the variable where we store the area.

# Complexity

- Time complexity: O(n)

- Space complexity: 1

# Code

```python []
class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        res = 0
        i, j = 0, len(height) - 1
        while i < j:
            area = (j-i) * min(height[i],height[j])
            res = max(res,area)
            if height[i] < height[j]:
                i += 1
            else:
                j -= 1
        return res
```
