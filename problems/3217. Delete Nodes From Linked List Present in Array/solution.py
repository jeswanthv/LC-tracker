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
