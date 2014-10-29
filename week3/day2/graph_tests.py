import unittest
from graph import DirectedGraph


class GraphTest(unittest.TestCase):
    def setUp(self):
        self.graph = DirectedGraph()

    def test_add_edge(self):
        self.graph.add_edge('A', 'B')
        self.assertTrue(('A', 'B') in self.graph.edges)

    def test_get_neighbours(self):
        self.graph.add_edge('A', 'B')
        self.graph.add_edge('A', 'C')
        self.graph.add_edge('D', 'A')
        self.assertEqual(self.graph.get_neighbours('A'), {'B', 'C'})

    def test_path_between(self):
        self.graph.add_edge('A', 'B')
        self.graph.add_edge('C', 'B')
        self.graph.add_edge('D', 'A')
        self.assertTrue(self.graph.path_between('D', 'B'))
        self.assertFalse(self.graph.path_between('D', 'C'))


if __name__ == "__main__":
    unittest.main()
