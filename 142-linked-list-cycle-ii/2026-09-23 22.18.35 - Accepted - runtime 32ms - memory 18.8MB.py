# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head==None:
            return None
        if head.next==None:
            return None
        fast=head
        slow=head
        while fast and fast.next:
            
            fast=fast.next.next
    
            slow=slow.next
            if fast==slow:
                break
        else:
            return None
            
        
        head1=head
        while head1!=fast:
            head1=head1.next
            fast=fast.next
        return head1
            