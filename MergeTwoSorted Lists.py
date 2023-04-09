# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:

    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:

        if list1 == None:
            return list2
        if list2 == None:
            return list1 
        
        if list1.val <= list2.val:
            new_list = ListNode(list1.val,None)
            head = new_list
            list1 = list1.next
        else:
            new_list = ListNode(list2.val,None)
            head = new_list
            list2 = list2.next

        while list1 != None and list2 != None:
            if list1.val == list2.val:
                node1, node2  = ListNode(list1.val,None), ListNode(list2.val,None)
                head.next, head.next.next = node1,node2
                head = head.next.next
                list1, list2 = list1.next,list2.next
            elif list1.val < list2.val:
                node1 = ListNode(list1.val,None)
                head.next = node1
                head = head.next
                list1 = list1.next
            elif list2.val < list1.val:
                node2 = ListNode(list2.val,None)
                head.next = node2
                head = head.next
                list2 = list2.next
            
        while list1 != None:
            node = ListNode(list1.val,None)
            head.next = node
            head = head.next
            list1 = list1.next
        while list2 != None:
            node = ListNode(list2.val,None)
            head.next = node
            head = head.next
            list2 = list2.next

        return new_list
      
"""
Example 1:
Input: list1 = [1,2,4], list2 = [1,3,4]
Output: [1,1,2,3,4,4]
Example 2:

Input: list1 = [], list2 = []
Output: []
Example 3:

Input: list1 = [], list2 = [0]
Output: [0]

"""
