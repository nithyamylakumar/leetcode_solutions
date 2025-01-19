from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        current = dummy

        while list1 and list2:
            if list1.val < list2.val:
                current.next = list1
                list1 = list1.next
            else:
                current.next = list2
                list2 = list2.next
            current = current.next

        if list1:
            current.next = list1
        elif list2:
            current.next = list2

        return dummy.next

# Example usage:
node1 = ListNode(1)
node2 = ListNode(2)
node3 = ListNode(3)
node1.next = node2
node2.next = node3

node4 = ListNode(1)
node5 = ListNode(3)
node6 = ListNode(4)
node4.next = node5
node5.next = node6

solution_object = Solution()
merged_list = solution_object.mergeTwoLists(node1, node4)  # Correct method call

# Print the merged list:
current_node = merged_list
while current_node:
    print(current_node.val, end=" -> ")
    current_node = current_node.next
