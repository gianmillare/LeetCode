def mergeTwoLists(l1, l2):
    l3 = ListNode(0)
    pointer = l3

    while True:
        if l1 is None and l2 is None:
            break
        elif l2 is None:
            pointer.next = l1
            break
        elif l1 is None:
            pointer.next = l2
            break
        else:
            smaller_value = 0
            if l1.val < l2.val:
                smaller_value = l1.val
                l1 = l1.next
            else:
                smaller_value = l2.val
                l2 = l2.next

            new_node = ListNode(smaller_value)
            pointer.next = new_node
            pointer = pointer.next

    return l3.next





x = [1, 2, 4]
y = [1, 3, 4]
mergeTwoLists(x, y)