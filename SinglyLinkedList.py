# A singly linked list object in python


class LLNode(object):
    def __init__(self, data=None, next=None):
        self.data = data
        self.next_node = next

    def get_data(self):
        return self.data

    def get_next(self):
        return self.next_node

    def set_next(self, new_next):
        self.next_node = new_next


class LinkedList(object):
    
