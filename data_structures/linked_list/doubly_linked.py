""" doubly linked list. """
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
        current_node = self.head
        while current_node:
            # iterate till end -> temp-data is not none
            current_node = current_node.next

        return "Linked List Traversal."


    def add_node(self,node_data):
        """ add node to after head. """
        # create node
        new_node = Node(data=node_data)
        # add node
        if self.head is None:
            # head not created -> assign as head
            self.head = new_node
        else:
            # point head to new-node and point new-node to previous first node
            prev_second_node = self.head.next
            self.head.next = new_node
            new_node.next = prev_second_node
            new_node.prev = self.head
            prev_second_node.prev = new_node

        return f"Node {new_node} Added after head."


    def append_node(self,node_data):
        """ add node at end. """
        # create node
        new_node = Node(data=node_data)
        # add node
        if self.head is None:
            # head not created -> assign as head
            self.head = new_node
        else:
            current_node = self.head
            while current_node:
                if not current_node.next:
                    # if current-node has no next-node
                    current_node.next = new_node
                    new_node.prev = current_node
                else:
                    continue

        return f"Node {new_node} Added at end."


    def insert_head(self,node_data):
        """ Insert a Node at the Beginning. """
        # create node
        new_node = Node(data=node_data)
        # add node
        if self.head is None:
            # head not created -> assign as head
            self.head = new_node
        else:
            # point original head to new node
            head_node = self.head
            new_node.next = head_node
            head_node.prev = new_node
            # make new node as head
            self.head = new_node

        return f"Node {new_node} Added as Head."


    # def insert_node(self,node_data,relative_node):
    #     """ Insert a Node after a Given Node in. """
    #     # create node
    #     new_node = Node(data=node_data)
    #     current_node = self.head
    #     if current_node.data == relative_node.data
    #     # assign prev-node-next to new-node-next
    #     prev_node_next_node = prev_node.next
    #     new_node.next = prev_node_next_node
    #     new_node.prev = prev_node

        
    #     return f"Node {new_node} Added after {prev_node}."


    # def insert_tail(self,node_data):
    #     """ Insert a Node at the End of. """
    #     # create node
    #     new_node = Node(data=node_data)
    #     # add node
    #     if self.head is None:
    #         # head not created -> assign as head
    #         self.head = new_node
    #     else:
    #         # iterate till end
    #         temp_tail = self.head.next
    #         while temp_tail:
    #             temp_tail = temp_tail.next
    #         temp_tail.next = new_node

    #     return f"Node {new_node} Added as Tail."


    # def reverse(self):
    #     """ Revserse a linked list. """
    #     # start fro head
    #     current_node = self.head
    #     prev_node = None
    #     next_node = None
    #     # iterate through nodes
    #     while current_node.next:
    #         # assign new nodes
    #         prev_node = current_node
    #         next_node = current_node.next
    #         # point next-node to prev-node
    #         next_node.next = prev_node
    #         # assign next-node to current-node
    #         current_node = next_node
    #     # tail node is th last current-node -> assign as head-node
    #     self.head = current_node

    #     return "Linked list revered."


    # def delete_node_data(self,deletenode_data):
    #     """ Delete node from list. """
    #     if self.head is None:
    #         # list is empty
    #         return "Empty List."
    #     if self.head.data == deletenode_data:
    #         # head-data is the delete-data
    #         new_head = self.head.next
    #         # make new head
    #         self.head = new_head
    #     else:
    #         current_node = self.head
    #         while current_node.next:
    #             # iterate through nodes and check next node
    #             next_node = current_node.next
    #             if next_node.data == deletenode_data:
    #                 # point next-to-next node to current node
    #                 next_next_node = next_node.next
    #                 current_node.next = next_next_node
    #             else:
    #                 continue

    #     return f"Node Data {deletenode_data} Deleted."


    # def delete_node_position(self,deletenode_position):
    #     """ Delete node at a given position. """
    #     node_index = 0
    #     if self.head is None:
    #         # list is empty
    #         return "Empty List."
    #     # if head to be deleted
    #     if deletenode_position==0:
    #         # assign second node as head
    #         second_node = self.head.next
    #         self.head = second_node
    #     else:
    #         current_node = self.head
    #         while current_node.next:
    #             # iterate till the end
    #             # index position of next node is to be deleted
    #             if (node_index+1) == deletenode_position:
    #                 next_next_node = current_node.next.next
    #                 # point current node to next-next node
    #                 current_node.next = next_next_node
    #                 break

    #     return f"Node at position {deletenode_position} Deleted."
