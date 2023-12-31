"""
custom hash function
"""

class CustomHashFunction:
    """
    create/manage
    """
    def __init__(self,size):
        """
        create empty hash table
        """
        self.size = size
        self.hashtable = [0,]*size


    def hash_function(self,key):
        """ 
        function to return index value for a key. 
        -> index < size
        """
        def index_function(key_value):
            return key_value%int(10*int(len(str(key_value))))

        hash_value = index_function(key_value=key)
        return hash_value


    def add_element(self,key: int,data) -> bool:
        """ add element or return false. """
        index = self.hash_function(key=key)
        if (index<self.size) and (self.hashtable[index].isinstance(list)):
            self.hashtable[index] = [key,data]
            return True
        return False


    def remove_element(self,key: int) -> bool:
        """ remove element or return false. """
        index = self.hash_function(key=key)
        if (index<self.size) and (self.hashtable[index].isinstance(list)):
            self.hashtable[index] = 0
            return True
        return False


    def check_hashtale(self) -> bool:
        """ check hashtable"""
        print(self.hashtable)
        return True
