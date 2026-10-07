# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        length1=0
        length2=0
        head1=headA
        head2=headB
        while head1!=None:
            length1+=1
            head1=head1.next
        while head2!=None:
            length2+=1
            head2=head2.next
        temp1=headA
        temp2=headB
        if length1>length2:
            step=length1-length2
            for i in range(step):
                temp1=temp1.next
        else:
            step=length2-length1
            for i in range(step):
                temp2=temp2.next
        while temp1!=temp2:
            temp1=temp1.next
            temp2=temp2.next
        return temp1
        