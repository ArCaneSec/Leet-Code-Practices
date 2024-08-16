class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, list1: ListNode, list2: ListNode) -> ListNode:
        first = ListNode()
        head = first

        while list1 and list2:
            if list1.val > list2.val:
                head.next = list2
                list2 = list2.next
            else:
                head.next = list1
                list1 = list1.next
            
            head = head.next
        
        if list1:
            head.next = list1
        else:
            head.next = list2
        
        return dummy.next
    

list1 = ListNode(0)
list2 = ListNode(0)
sort = Solution().mergeTwoLists(list1, list2)
while sort is not None:
    print(sort.val)
    sort = sort.next