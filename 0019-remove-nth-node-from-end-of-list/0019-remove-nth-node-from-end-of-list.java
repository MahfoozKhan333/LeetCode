// class ListNode {
//     int val;
//     ListNode next;
//     ListNode(int x) {
//         val = x;
//     }
// }

public class Solution {
    public ListNode removeNthFromEnd(ListNode head, int n) {
        ListNode dummyList = new ListNode(0);
        dummyList.next = head;
        ListNode first = dummyList;
        ListNode second = dummyList;
        
        for (int i = 0; i <= n; i++) {
            first = first.next;
        }
        
        while (first != null) {
            first = first.next;
            second = second.next;
        }
        
        second.next = second.next.next;
        return dummyList.next;
    }
}
