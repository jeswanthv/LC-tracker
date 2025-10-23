class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        res = 0
        i, j = 0, len(height) - 1
        while i < j:
            area = (j-i) * min(height[i], height[j])
            res = max(res, area)
            if height[i] < height[j]:
                i += 1
            else:
                j -= 1
        return res
