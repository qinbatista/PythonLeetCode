
import collections
from typing import List, Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random


class LinkedList:
    def __init__(self) -> None:
        pass

    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        cur = head
        prev = None
        while cur.next:
            next = cur.next
            cur.next = prev
            prev = cur
            cur = next
        return cur.next

    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        tail = dummy
        while list1 and list2:
            if list1.val < list2.val:
                tail.next = list1
                list1 = list1.next
            else:
                tail.next = list2
                list2 = list2.next
            tail = tail.next
        if list1:
            tail.next = list1
        elif list2:
            tail.next = list2
        return dummy.next

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
        dummy = ListNode(0,head)
        left = dummy
        right = head
        while n > 1 and right:
            left = left.next
            n -= 1
        # while right:
        #     left = left.next
        #     right = right.next
        left.next = left.next.next
        return dummy.next

    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        dic = {None:None}
        cur = head
        while cur:
            copy = ListNode(cur.val)
            dic[cur] = copy
            cur = cur.next
        while cur:
            copy = dic[cur]
            copy.next = dic[cur.next]
            copy.random = dic[cur.random]
            cur = cur.next



    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        cur = dummy
        carry = 0
        while l1 or l2 or carry:
            v1 = l1.val if l1 else 0
            v2 = l2.val if l2 else 0
            value = v1+v2+carry
            carry = value//10
            value = value % 10
            cur.next = ListNode(value)
            cur = cur.next
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
        return dummy.next

    def hasCycle(self, head: Optional[ListNode]) -> bool:
        slow, fast = head, head.next
        while slow.next and fast.next:
            if slow == fast:
                return True
            slow = slow.next
            fast = fast.next
        return False


    def findDuplicate(self, nums: List[int]) -> int:
        slow, fast = 0, 0
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:
                break
        slow2 = 0
        while True:
            slow = nums[slow]
            slow2 = nums[slow2]
            if slow == slow2:
                return slow2


class Node:
    def __init__(self, key, val: int):
        self.key, self.val = key, val
        self.prev = self.next = None


class LRUCache:

    def __init__(self, capacity: int):
        self.cap = capacity
        self.cache = {}

        # left = LRU, right = most recent
        self.left, self.right = Node(0, 0), Node(0, 0)
        self.left.next, self.right.prev = self.right, self.left

    def remove(self, node):
        prev, nxt = node.prev, node.next
        prev.next, nxt.prev = nxt, prev

    def insert(self, node):
        prev, nxt = self.right.prev, self.right
        prev.next = nxt.prev = node
        node.next, node.prev = nxt, prev

    def get(self, key: int) -> int:
        if key in self.cache:
            self.remove(self.cache[key])
            self.insert(self.cache[key])
            return self.cache[key].val
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.remove(self.cache[key])
        self.cache[key] = Node(key, value)
        self.insert(self.cache[key])

        if len(self.cache) > self.cap:
            # remove from the list and delete the LRU from the hashmap
            lru = self.left.next
            self.remove(lru)
            del self.cache[lru.key]


if __name__ == "__main__":
    tp = LinkedList()
    node7 = ListNode(7, None)
    node6 = ListNode(6, node7)
    node5 = ListNode(5, node6)
    node4 = ListNode(4, node5)
    node3 = ListNode(3, node4)
    node2 = ListNode(2, node3)
    node1 = ListNode(1, node2)
    # node1.next = node2
    # node2.next = node3
    # node3.next = node4
    # node4.next = node5
    # print(tp.reorderList(node1))
    print(tp.removeNthFromEnd(node1, 4))
    # print(tp.findDuplicate([1, 3, 4, 2, 2]))
    # print(tp.reverseList())
    # print(tp.twoSum([2,3,4], 6))
    # print(tp.maxArea([1,8,6,2,5,4,8,3,7]))
