from neo4j.v1 import GraphDatabase, basic_auth

class GraphConnection:
    
    def __init__(self, location, password):
        self.driver = GraphDatabase.driver(location, auth=basic_auth("neo4j", password))

    def insert(self, node):
        session = self.driver.session()
        try:
            query = node.create_statement["query"]
            params = node.create_statement["params"]
            session.run(query, params).consume()
        except:
            print "error, probably a constraint was violated\n"
        finally:
            session.close()
