class Node:
    
    @property
    def create_statement(self):
        raise NotImplementedError("Node subclasses must implement create_statement")
