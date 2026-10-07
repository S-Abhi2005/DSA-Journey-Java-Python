# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeElements(self, head, val):
        """
        :type head: Optional[ListNode]
        :type val: int
        :rtype: Optional[ListNode]
        """
    
        newNode=ListNode()
    
        
        if head==None:
            return 
        newNode.next=head
        head=newNode
        
        
        while head!=None and head.next!=None:
            if head.next.val==val:
                head.next=head.next.next
                    
            else: 
                head=head.next
        
        return newNode.next
            
            