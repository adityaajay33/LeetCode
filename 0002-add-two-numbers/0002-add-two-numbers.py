# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        currentL1, currentL2 = l1, l2
        headL3 = ListNode()
        currentL3 = headL3
        carryOver = 0
        while currentL1!=None and currentL2!=None:

            currentL3.val = (carryOver + currentL1.val + currentL2.val)%10
            carryOver = int((carryOver + currentL1.val + currentL2.val)/10)

            if currentL1.next==None and currentL2.next==None and carryOver==0:
                return headL3
            elif currentL1.next==None and currentL2.next==None and carryOver!=0:
                currentL3.next = ListNode(val=carryOver)
            elif currentL1.next==None:
                currentL1.next = ListNode()
            elif currentL2.next==None:
                currentL2.next = ListNode()

            currentL3.next = ListNode(val=carryOver)
            currentL3, currentL2, currentL1 = currentL3.next, currentL2.next, currentL1.next      

        return headL3

            