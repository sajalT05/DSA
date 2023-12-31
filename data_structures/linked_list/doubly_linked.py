""" doubly circular linked. """
import dataclasses



@dataclasses.dataclass
class Node:
    """
    node of a linked list
    """
    def __init__(self,data):
        """
        assign data and prev & next node
        """
        self.data = data
        self.next = None
        self.prev = None


@dataclasses.dataclass
class DoublyLinkedList:
    """
    create/manage
    """
    def __init__(self):
        """
        create empty
        head ->
        """
        self.head = None


    def traverse_iteration(self):
        """ Traverse through (iteration)."""
        # allocate temp-value to head
        head_node = self.head
        current_node = head_node
        while current_node:
            # iterate till end -> temp-data is not none
            # check if not head-node
            if current_node != head_node:
                current_node = current_node.next
            else:
                break

        return "Linked List Traversed."


    def add_node(self,node_data):
        """ add node after head. """
        # create node
        new_node = Node(data=node_data)
        head_node = self.head
        # add node
        if head_node is None:
            # head not created -> assign as head
            self.head = new_node
        else:
            # point head to new-node and point new-node to previous first node
            prev_second_node = head_node.next
            head_node.next = new_node
            new_node.prev = head_node
            new_node.next = prev_second_node
            prev_second_node.prev = new_node

        return f"Node {new_node} Added after head."


    def append_node(self,node_data):
        """ add node at end. """
        # create node
        new_node = Node(data=node_data)
        head_node = self.head
        # add node
        if head_node is None:
            # head not created -> assign as head
            self.head = new_node
        else:
            current_node = head_node
            while current_node:
                if not current_node.next:
                    # if current-node has no next-node
                    current_node.next = new_node
                else:
                    continue

        return f"Node {new_node} Added at end."
