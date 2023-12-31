""" circular linked. """
import dataclasses



@dataclasses.dataclass
class Node:
    """
    node of a linked list
    """
    def __init__(self,data):
        """
        assign data and next node
        """
        self.data = data
        self.next = None


@dataclasses.dataclass
class CircularLinkedList:
    """
    create/manage
    """
    def __init__(self):
        """
        create empty
        last ->
        """
        self.tail = None


    def empty_add(self,node):
        """ Add node to empty list. """
        if self.tail is not None:
            return self.tail
        self.tail = node
        self.tail.next = self.tail

        return self.tail



    def traverse(self) -> None or str:
        """ Traverse through (iteration)."""
        # allocate temp-value to head
        tail_node = self.tail
        if tail_node is None:
            return None
        current_node = tail_node.next
        while current_node:
            current_node = current_node.next
            if current_node == tail_node.next:
                break

        return "Linked List Traversed."


    def append_node(self,node_data):
        """ add node after tail. """
        # create node
        new_node = Node(data=node_data)
        tail_node = self.tail
        # add node
        if tail_node is None:
            # tail not created -> assign as tail
            return self.empty_add(node=new_node)
        # point head to new-node and point new-node to previous first node
        tail_next_node = tail_node.next
        tail_node.next = new_node
        self.tail = new_node
        new_node.next = tail_next_node

        return f"Node {new_node} Added after tail."

    def insert_node(self,node_data,list_node_data):
        """ Insert node aftr a node. """
        tail_node = self.tail
        new_node = Node(data=node_data)
        if tail_node is None:
            return None
        current_node = tail_node.next
        while current_node:
            if current_node.data == list_node_data:
                # data matches -> add node
                next_node = current_node.next
                current_node.next = new_node
                new_node.next = next_node
                # make new tail
                if current_node == self.tail:
                    self.tail = new_node
                break
            current_node = current_node.next
            if current_node == tail_node.next:
                break

        return f"Node {new_node} Added after tail."


    def delete_node(self,list_node_data):
        """ Delete a node. """
        tail_node = self.tail
        if tail_node is None:
            return None            
        current_node = tail_node
        while current_node:
            if current_node.data == list_node_data:
                # tail node
                if current_node == tail_node:
                    self.tail = None
                    self.tail.next = None
                else:
                    # next node
                    next_node = current_node.next
                    # previous node
                    prvs_node = current_node.next
                    while prvs_node != current_node:
                        prvs_node = prvs_node.next
                    # point previous-node to next-node
                    prvs_node.next = next_node

        return f"Node {list_node_data} Deleted."
