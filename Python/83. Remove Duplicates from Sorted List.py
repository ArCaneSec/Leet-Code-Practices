# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution(object):
    def deleteDuplicates(self, head):

        current = head
        prev = None

        while current is not None:
            if prev is not None and prev.val != current.val:
                prev = current
            else:
                if prev is None:
                    prev = current
                else:
                    prev.next = current.next

            current = current.next

        return head
