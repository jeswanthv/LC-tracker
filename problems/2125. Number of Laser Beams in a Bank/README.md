[problem link](https://leetcode.com/problems/number-of-laser-beams-in-a-bank/description)

# Approach

- Count All '1' in every row and store it in one array `counts`.
- Multiply current val and adjacent val and store it in `total` variable. You can do this with zip function.
- Return `total`

# Complexity

- Time complexity: O(N \* M) The list comprehension iterates through all N rows, and for each row, row.count("1") takes O(M) time to scan the string.

- Space complexity:O(N)

# Code

```python3 []
class Solution:
    def numberOfBeams(self, bank: List[str]) -> int:
        counts = [row.count("1") for row in bank if "1" in row]
        total = 0

        for p, c in zip(counts, counts[1:]):
            total += p * c

        return total
```
