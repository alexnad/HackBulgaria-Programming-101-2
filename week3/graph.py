

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
        searched_nodes = set()
        step = 1
        unsearched_nodes = [nodeA, step]
        path_exists = False

        while unsearched_nodes and not path_exists:
            node = unsearched_nodes[0]
            unsearched_nodes.remove(node)

            if isinstance(node, int) and unsearched_nodes:
                step += 1
                unsearched_nodes.append(step)
                continue

            searched_nodes.add(node)
            new_batch = self.get_neighbours(node)

            if nodeB in new_batch:
                path_exists = True
                break
            x = [node for node in new_batch if node not in searched_nodes]
            unsearched_nodes.extend(x)

        if not path_exists:
            step = 0

        return (path_exists, step)

    def __str__(self):
        return str(self.nodes) + '\n' + str(self.edges)
