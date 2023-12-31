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
        queue_length = len(self.queue)
        if queue_length!=0:
            return queue_length
        return None


    def push_item(self,data):
        """ add item to queue's top. """
        return self.queue.append(data)


    def pop_item(self):
        """ remove ite from queue's top. """
        if self.check_stack_empty() is not None:
            return self.queue.pop()
        return "Empty queue."


    def top_item(self):
        """ return top item of queue. """
        if self.check_stack_empty() is not None:
            return self.queue[-1]
        return "Empty queue."


    def last_item(self):
        """ return last item of queue. """
        if self.check_stack_empty() is not None:
            return self.queue[0]
        return "Empty queue."
