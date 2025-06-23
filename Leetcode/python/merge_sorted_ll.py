from Leetcode.python import ListNode


def merge(l1, l2):
    dummy = ListNode() = node
    t1,t2 = l1,l2
    while not t1 and not t2:
        if t1.val <= t2.val:
            node.next = t1
            t1 = t1.next
        else:
            node.next = t2
            t2 = t2.next
        node = node.next
    node.next = l1 or l2
    return dummy.next