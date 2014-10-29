

class DirectedGraph:
    def __init__(self):
        self.nodes = set()
        self.edges = set()

    def add_edge(self, nodeA, nodeB):
        self.nodes.add(nodeA)
        self.nodes.add(nodeB)
        self.edges.add((nodeA, nodeB))

    def get_neighbours(self, node):
        return {edge[1] for edge in self.edges if edge[0] == node}

    def path_between(self, nodeA, nodeB):
        searched_nodes = {}
        unsearched_nodes = [nodeA]
        path_exists = False
        while unsearched_nodes and not path_exists:
            for node in unsearched_nodes:
                unsearched_nodes.remove(node)
                new_batch = self.get_neighbours(node)
                if nodeB in new_batch:
                    path_exists = True
                    break
                x = [node for node in new_batch if node not in searched_nodes]
                unsearched_nodes.extend(x)

        return path_exists

    def __str__(self):
        return str(self.nodes) + '\n' + str(self.edges)
