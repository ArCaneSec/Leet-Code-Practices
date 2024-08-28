class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __iter__(self):
        self._current = self
        return self

    def __next__(self):
        if self._current is None:
            raise StopIteration()
        
        val = self._current.val
        self._current = self._current.next
        return val

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
        
        return first.next
    

list1 = ListNode(0)
current = list1
for i in range(1, 6):
    current.next = ListNode(i)
    current = current.next

for i in list1:
    print(i)
for i in list1:
    print(i)
# print(next(list1))
# print(next(list1))
# print(next(list1))