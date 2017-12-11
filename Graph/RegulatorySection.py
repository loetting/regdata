from Node import Node
from rake_nltk import Rake

class RegulatorySection(Node):

    def __init__(self, head, text):
        self.head = head
        self.text = text

    @property
    def create_statement(self):
        return {"query": "CREATE (regulation:Regulation {head: {head}, text: {text}})", "params": {"head": self.head, "text": self.text}}