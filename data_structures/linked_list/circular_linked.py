""" circular linked. """
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