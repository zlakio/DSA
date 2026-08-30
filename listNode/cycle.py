class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def isCycle(head):
        fast = head
        slow = head
        while fast and fast.next.next is None:
            slow = slow.next
            fast = fast.next.next

        if slow == fast:
            return True
        
        return False


head = ListNode(val=2)
head.next = ListNode(3)

print(ListNode.isCycle(head))
