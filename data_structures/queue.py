""" queue. """
import dataclasses



@dataclasses.dataclass
class Queue:
    """
    create/manage
    """
    def __init__(self):
        """
        cretae empty stack
        """
        self.queue = []

    def check_stack_empty(self):
        """ check if stack is empty. """
        stack_length = len(self.stack)
        if stack_length!=0:
            return stack_length
        return 0

    def push_item(self,data):
        """ add item to stack's top. """
        return self.stack.append(data)

    def pop_item(self):
        """ remove ite from stack's top. """
        if self.check_stack_empty()!=0:
            return self.stack.pop()
        return "Empty Stack."

    def top_item(self):
        """ return top item of stack. """
        if self.check_stack_empty()!=0:
            return self.stack[-1]
        return "Empty Stack."
