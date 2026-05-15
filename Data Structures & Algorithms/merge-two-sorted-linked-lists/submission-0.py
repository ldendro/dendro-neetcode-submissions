# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        def merge(listA, listB):
            if not listA:
                return listB
            elif not listB:
                return listA
            else:
                if listA.val <= listB.val:
                    listA.next = merge(listA.next, listB)
                    return listA
                else:
                    listB.next = merge(listA, listB.next)
                    return listB

        dummy = ListNode()
        dummy.next = merge(list1, list2)
        return dummy.next