class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        # Create dummy head node
        dummy = ListNode(0)
        curr = dummy
        carry = 0
        
        # Process until both lists are empty and no carry remains
        while l1 or l2 or carry:
            # Get values
            x = l1.val if l1 else 0
            y = l2.val if l2 else 0
            
            # Calculate sum and carry
            total = x + y + carry
            carry = total // 10
            
            # Create new node
            curr.next = ListNode(total % 10)
            curr = curr.next
            
            # Move to next nodes if available
            if l1: l1 = l1.next
            if l2: l2 = l2.next
        
        return dummy.next