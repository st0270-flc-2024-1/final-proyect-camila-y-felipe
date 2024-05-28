import unittest
from main import compute_first, compute_first_string, compute_follow
from collections import defaultdict

class TestGrammarParser(unittest.TestCase):
    def read_grammar(self, filename):
        with open(filename, 'r') as file:
            return file.read()
    
    def test_compute_first(self):
        productions = {
            'S': [['A', 'B']],
            'A': [['a'], ['e']],
            'B': [['b']]
        }
        first = defaultdict(set)
        visited = set()
        compute_first('S', productions, first, visited)
        self.assertEqual(first['S'], {'a', 'b', 'e'})
        compute_first('A', productions, first, visited)
        self.assertEqual(first['A'], {'a', 'e'})
        compute_first('B', productions, first, visited)
        self.assertEqual(first['B'], {'b'})

    def test_compute_first_string(self):
        productions = {
            'S': [['A', 'B']],
            'A': [['a'], ['e']],
            'B': [['b']]
        }
        first = defaultdict(set)
        visited = set()
        for non_terminal in productions:
            compute_first(non_terminal, productions, first, visited)
        result = compute_first_string(['A', 'B'], productions, first)
        self.assertEqual(result, {'a', 'b', 'e'})

    def test_compute_follow(self):
        productions = {
            'S': [['A', 'B']],
            'A': [['a'], ['e']],
            'B': [['b']]
        }
        first = defaultdict(set)
        follow = defaultdict(set)
        visited = set()
        for non_terminal in productions:
            compute_first(non_terminal, productions, first, visited)
        compute_follow('S', productions, first, follow, 'S')
        self.assertEqual(follow['S'], {'$'})
        compute_follow('A', productions, first, follow, 'S')
        self.assertEqual(follow['A'], {'b'})
        compute_follow('B', productions, first, follow, 'S')
        self.assertEqual(follow['B'], {'$', 'a'})

if __name__ == '__main__':
    unittest.main()