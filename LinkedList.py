
import collections
from typing import List, Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class LinkedList:
    def __init__(self) -> None:
        pass

    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        cur = head
        prev = None
        while cur:
            tmp = cur.next
            cur.next = prev
            prev = cur
            cur = tmp
        return prev

if __name__ == "__main__":
    tp = LinkedList()
    print(tp.reverseList())
    # print(tp.twoSum([2,3,4], 6))
    # print(tp.maxArea([1,8,6,2,5,4,8,3,7]))
