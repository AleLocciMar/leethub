# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        auxl1 = ""
        auxl2 = ""

        while l1:
           auxl1 = str(l1.val) + auxl1  
           l1 = l1.next
           
        while l2:
           auxl2 =  str(l2.val)  + auxl2  
           l2 = l2.next

        auxSoma = str(int(auxl1) + int(auxl2))
        auxSoma = auxSoma[::-1]
        sentinela = ListNode(0)
        atual = sentinela
    
        for c in auxSoma:
            atual.next = ListNode(int(c))
            atual = atual.next

        return sentinela.next 
        