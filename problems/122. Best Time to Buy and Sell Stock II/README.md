[problem link](https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii/description/)

# Intuition

- We just need to keep track of price differences between two day prices if the later one is bigger than previous one.
- So, We can use two pointers since we need to keep track between two prices.

# Approach

- Use `profit` var to keep track of total profit/
- Use 2 pointers `l` and `r`:
  - Track price diff between them if `prices[r] > prices[l]` and assign it to `profit`
  - Else, move to next part `l=r` and `r+=1`
- Finally, return `profit` var.

# Complexity

- Time complexity: O(n)

- Space complexity: O(1)

# Code

```python3 []
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        pro = 0
        l, r = 0, 1
        while r < len(prices):
            if prices[r] > prices[l]:
                p = prices[r] - prices[l]
                pro += p
            l = r
            r += 1
        return pro

```
