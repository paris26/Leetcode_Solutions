
struct ListNode {
      int val;
      ListNode *next;
      ListNode() : val(0), next(nullptr) {}
      ListNode(int x) : val(x), next(nullptr) {}
      ListNode(int x, ListNode *next) : val(x), next(next) {}
};

class Solution {
public:
    ListNode* addTwoNumbers(ListNode* l1, ListNode* l2) {
        ListNode* dummy = new ListNode(0);
        ListNode* curr = dummy;
        int carry = 0;

        while( l1 || l2 || carry ){
            int value1 = ( l1 ? l1->val : 0 ) ;
            int value2 = ( l2 ? l2->val : 0 ) ;

            int total = value1 + value2 + carry;
            carry = total / 10;
            int digit = total % 10 ;

            curr->next = new ListNode(total % 10);
            curr = curr->next;

            if(l1) l1 = l1->next;
            if(l2) l2 = l2->next;
         }

         return dummy->next;
};

};