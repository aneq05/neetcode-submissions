# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if not head:
            return []

        nodes = []
        
        # wyciągamy elementy do osobnej listy
        current = head
        while current:
            nodes.append(current)
            current = current.next

        # wyciągamy długość aby potem móc pozmieniać indeksy
        n = len(nodes)
        left, right = 0, n-1

        # zmiana kolejności
        while left < right:
            nodes[left].next = nodes[right]
            left += 1

            if left == right:
                break
            
            nodes[right].next = nodes[left]
            right -= 1
        
        nodes[left].next = None
        