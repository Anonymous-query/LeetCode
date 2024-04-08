from typing import Any

class Node:
    def __init__(self, data: Any, next_node=None) -> None:
        self.data = data
        self.next = next_node

class LinkedList:
    def __init__(self, head = None) -> None:
        self.head = head

    def linked_append(self, data: Any) -> None:
        print("New append happening", data)
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        
        last_node = self.head
        while last_node.next:
            last_node = last_node.next

        last_node.next = new_node

    def linked_insert(self, data: Any) -> None:
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def linked_remove(self, data: Any) -> None:
        current_node = self.head

        if current_node and current_node.data == data:
            self.head = current_node.next
            current_node = None
            return

        previous_node = None
        while current_node and current_node.data != data:
            previous_node = current_node
            current_node = current_node.next
            
        if current_node is None:
            return

        previous_node.next = current_node.next
        current_node = None

    def linked_reverse(self) -> None:
        previous_node = None
        current_node = self.head
        while current_node:
            next_node = current_node.next
            current_node.next = previous_node

            previous_node = current_node
            current_node = next_node
        
        self.head = previous_node

    def linked_recursive_revserse(self) -> None:
        def _linked_recursive_revserse(current_node: Node, prevous_node: None = None) -> Node:
            if not current_node:
                return prevous_node

            next_node = current_node.next
            current_node.next = prevous_node
            prevous_node = current_node
            current_node = next_node
            return _linked_recursive_revserse(current_node, prevous_node)
        
        self.head = _linked_recursive_revserse(self.head, None)

    def linked_show(self) -> None:
        current_node = self.head

        while current_node:
            print(current_node.data)
            current_node = current_node.next

if __name__ == "__main__":
    linked_obj = LinkedList()
    linked_obj.linked_append(3)
    linked_obj.linked_append(5)
    linked_obj.linked_insert(6)
    linked_obj.linked_append(2)
    linked_obj.linked_insert(7)
    linked_obj.linked_show()
    linked_obj.linked_reverse()
    print("after")
    linked_obj.linked_show()
    print("recursive")
    linked_obj.linked_recursive_revserse()
    linked_obj.linked_show()