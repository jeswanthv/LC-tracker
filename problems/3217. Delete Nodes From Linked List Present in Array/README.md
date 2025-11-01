[problem link](https://leetcode.com/problems/delete-nodes-from-linked-list-present-in-array/description)

# Intuition

- Use Simple pointer traverse solution.

# Approach

- Let's change array of `nums` into `set` to reduce time complexity of looking up number in array.
- Initialize `prev` pointer and traverse thought the link with `current` pointer.
- If you find the number in set, then simply point the `prev`.next to `current` next pointer. Else, simply assign `prev` to `current` pointer.
- Finally, assign `current` to next `current`.

# Complexity

- Time complexity: O(n)

- Space complexity: O(1)

# Code

```python3 []
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def modifiedList(self, nums: List[int], head: Optional[ListNode]) -> Optional[ListNode]:
        visit = set(nums)
        tmp = prev = ListNode(0, head)
        dummy = head
        while dummy:
            if dummy.val in visit:
                prev.next = dummy.next
            else:
                prev = dummy
            dummy = dummy.next
        return tmp.next

```
