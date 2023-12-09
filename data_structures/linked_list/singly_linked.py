"""singly linked list"""
import dataclasses

@dataclasses.dataclass
class Node:
    """
    node of a linked list
    """
    def __init__(self,data):
        """
        assign data and next value
        """
        self.data = data
        self.next = None

@dataclasses.dataclass
class SinglyLinkedList:
    """
    create/manage linked list
    """
    def __init__(self):
        """
        cretae empty linked list
        -> empty head & tail
        """
        self.head = None
        self.tail = None


    def add_node(self,node_data):
        """ add node to a linked list -> if head not created -> assign as head """
        # create node
        new_node = Node(data=node_data)
        # add node
        if self.head is None:
            # if head & tail not created -> assign as head & tail
            self.head = new_node
            self.tail = new_node
        else:
            # head & tail created -> assign after tail
            self.tail.next = new_node
