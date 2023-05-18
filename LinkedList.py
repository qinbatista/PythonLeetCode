
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

    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dump = ListNode()
        tail = dump
        while list1 and list2:
            if list1.val < list2.val:
                tail.next = list1
                tail = tail.next
            else:
                tail.next = list2
                tail = tail.next
            tail = tail.next
        if list1:
            tail.next = list1
        elif list2:
            tail.next = list2
        return dump.next

    def reorderList(self, head: Optional[ListNode]) -> None:
        slow = head
        fast = head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        second = slow.next
        prev = slow.next = None
        while second:
            tmp = second.next
            second.next = prev
            prev = second
            second = tmp
        first = head
        second = prev
        while second:
            tmp1, tmp2 = first.next, second.next
            first.next = second
            second.next = tmp1
            first, second = tmp1, tmp2

    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        left = dummy
        right = head
        while n>0 and right:
            right = right.next
            n-=1
        while right:
            left = left.next
            right = right.next
        left.next = left.next.next
        return dummy.next
if __name__ == "__main__":
    tp = LinkedList()
    node1 = ListNode(1, None)
    node2 = ListNode(2, None)
    node3 = ListNode(3, None)
    node4 = ListNode(4, None)
    node5 = ListNode(5, None)
    # node1.next = node2
    # node2.next = node3
    # node3.next = node4
    # node4.next = node5
    # print(tp.reorderList(node1))
    print(tp.removeNthFromEnd(node1, 2))
    # print(tp.reverseList())
    # print(tp.twoSum([2,3,4], 6))
    # print(tp.maxArea([1,8,6,2,5,4,8,3,7]))
