from typing import List, Any

class Node:
    def __init__(self, data: Any, next_node = None):
        self.data = data
        self.next = next_node

class LinkedList:
    def __init__(self, head=None) -> None:
        self.head = head

    def append(self, data:Any = None) -> None:
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        
        last_node = self.head
        while last_node.next:
            last_node = last_node.next

        last_node.next = new_node
    
    def insert(self, data: Any) -> None:
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def show_linked_list(self) -> None:
        current_node = self.head
        while current_node:
            print(current_node.data)
            current_node = current_node.next

    def remove_node(self, data:Any) -> None:
        current_node = self.head
        if current_node and current_node.data == data:
            self.head = current_node.next
            current_node = None
            return
        
        previous_node = None
        while current_node and current_node.data != data:
            previous_node =  current_node
            current_node = current_node.next

        if current_node is None:
            return
        
        previous_node.next = current_node.next
        current_node = None

    def reverse_linked_list(self) -> None:
        previous_node = None
        current_node = self.head
        while current_node:
            next_node = current_node.next
            current_node.next = previous_node

            previous_node = current_node
            current_node = next_node

        self.head = previous_node

    def recursive_revser_linked_list(self) -> None:
        def _recursive_revser_linked_list(current_node: Node, previous_node: None) -> Node:
            if not current_node:
                return previous_node
            
            next_node = current_node.next
            current_node.next = previous_node

            previous_node = current_node
            current_node = next_node
            return _recursive_revser_linked_list(current_node, previous_node)
        
        self.head = _recursive_revser_linked_list(self.head, None)


if __name__ == "__main__":
    linked_list = LinkedList()
    linked_list.append(5)
    linked_list.insert(6)
    linked_list.insert(7)
    linked_list.insert(8)
    linked_list.show_linked_list()
    print(f"After revers {linked_list.recursive_revser_linked_list()}")
    linked_list.show_linked_list()