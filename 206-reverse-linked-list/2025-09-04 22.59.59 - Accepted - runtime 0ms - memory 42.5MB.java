
 public class Solution {
//      public static class ListNode{
// int val;
// ListNode next;

// ListNode(int val){
//     this.val=val;
// }
//     }
   

   
    public ListNode reverseList(ListNode head) {
        if(head==null ||head.next==null)return head ;
        ListNode newhead=reverseList(head.next);
        head.next.next=head;
        head.next=null;
        return newhead;
    }
       
 
        
    }
