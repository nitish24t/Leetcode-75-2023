class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        myList = {}
        while head:
            if head not in myList:
                myList[head] = 0
            else:
                return head
            head = head.next
