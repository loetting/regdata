from Node import Node

class Test(Node):

    def __init__(self, value):
        self.value = value

    @property
    def create_statement(self):
        return {"query": "CREATE (test:Test {value: {value}})", "params": {"value": self.value}}