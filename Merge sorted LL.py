class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def merge_two_lists(list1: ListNode, list2: ListNode) -> ListNode:
    dummy = ListNode()
    current = dummy
    
    # Pointers to traverse the lists
    l1 = list1
    l2 = list2
    
    while l1 is not None and l2 is not None:
        if l1.val < l2.val:
            current.next = l1
            l1 = l1.next
        else:
            current.next = l2
            l2 = l2.next
        current = current.next
    
    if l1 is not None:
        current.next = l1
    else:
        current.next = l2
    
    return dummy.next

def create_linked_list(values):
    if not values:
        return None
    head = ListNode(values[0])
    current = head
    for value in values[1:]:
        current.next = ListNode(value)
        current = current.next
    return head

def linked_list_to_list(head):
    result = []
    current = head
    while current is not None:
        result.append(current.val)
        current = current.next
    return result

list1 = create_linked_list([1, 2, 4])
list2 = create_linked_list([1, 3, 4])
merged_list = merge_two_lists(list1, list2)
print(linked_list_to_list(merged_list))  
