"""
hash function
"""

class HashFunction:
    """
    create/manage
    """
    def __init__(self,size):
        """
        create empty hash table
        """
        self.size = size
        self.hashtable = [0,]*size

    def division_function(self,key,data):
        """ division method. """
        index = key%self.size
        self.hashtable[index] = [key,data]

    # def midsquare_function(self,key,data):
    #     """ mid-square method. """
    #     mid_value_length = int(len(str(self.size))-1)
    #     key_square = key*key
    #     index = str(key_square)[]
    #     self.hashtable[index] = [key,data]