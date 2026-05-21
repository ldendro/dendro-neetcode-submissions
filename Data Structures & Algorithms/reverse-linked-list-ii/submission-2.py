# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        dummy = ListNode()
        cur = head
        dummy.next = cur
        pre = dummy

        counter = 1
        while counter <= right:
            if counter + 1 == left:
                pre = cur
                cur = cur.next
            elif counter == left:
                prev = cur
                first = cur
                cur = cur.next
            elif left < counter < right:
                nxt = cur.next
                cur.next = prev
                prev = cur
                cur = nxt
            elif counter == right:
                pre.next = cur if pre else None
                first.next = cur.next
                cur.next = prev
            else:
                cur = cur.next
            counter += 1

        return dummy.next
