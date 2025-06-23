from Leetcode.python import ListNode
def remove(head: ListNode, n):
    dummy = ListNode()
    dummy.next = head
    left = dummy
    right = head
    while n>0:
        right = right.next
        n-=1
    while right:
        left = left.next
        right = right.next
    left.next = left.next.next
    return dummy.next