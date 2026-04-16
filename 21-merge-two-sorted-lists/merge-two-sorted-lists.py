# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
          # 1. Criamos um nó "boneco" para segurar o início da nova lista
        if list1 is None:
            return list2

        if list2 is None:
            return list1

        dummy = ListNode(0)
        # 2. O 'atual' é quem vai caminhar e construir a nova lista.
        atual = dummy

        while list1 and list2:
            if list1.val <= list2.val:
                atual.next = list1
                list1 = list1.next
            else:
                atual.next = list2
                list2 = list2.next

            atual = atual.next
        atual.next = list1 if list1 else list2

        return dummy.next
        