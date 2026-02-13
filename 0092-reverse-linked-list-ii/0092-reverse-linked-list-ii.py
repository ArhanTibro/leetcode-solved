# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        if head.next is None:
            return head
        i=1
        track={}
        curr=head
        st=None
        fin=None
        while curr:
            if i==left-1:
                st=curr
            if i>=left :
                track[i]=curr
            if i==right:
                fin=curr.next
                break
            curr=curr.next
            i+=1
        n=right
        if st is None:
            head=track[n]
            curr=head
            n-=1
            while n>=left:
                curr.next=track[n]
                curr=curr.next
                n-=1
            curr.next=fin
            return head
        
        while n>=left:
            st.next=track[n]
            st=st.next
            n-=1
        st.next=fin
        return head
            

        
        return head

        
