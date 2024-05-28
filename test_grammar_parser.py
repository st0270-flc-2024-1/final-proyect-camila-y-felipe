import unittest
from main import compute_first, compute_first_string, compute_follow
from collections import defaultdict

class TestGrammarParser(unittest.TestCase):
    productions = [
        {
            'S': [['A', 'B']],
            'A': [['a'], ['e']],
            'B': [['b']]
        },
        {
            'S': [['A', 'b'], ['B', 'c']],
            'A': [['a'], ['e']],
            'B': [['d']]
        },
        {
            'S': [['A', 'B', 'C']],
            'A': [['a'], ['e']],
            'B': [['b'], ['e']],
            'C': [['c']]
        }
    ]

    expected_first = [
        {
            'S': {'a', 'b'},
            'A': {'a', 'e'},
            'B': {'b'}
        },
        {
            'S': {'a', 'd', 'b'},
            'A': {'a', 'e'},
            'B': {'d'}
        },
        {
            'S': {'a', 'b', 'c'},
            'A': {'a', 'e'},
            'B': {'b', 'e'},
            'C': {'c'}
        }
    ]

    expected_follow = [
        {
            'S': {'$'},
            'A': {'b'},
            'B': {'$'}
        },
        {
            'S': {'$'},
            'A': {'b'},
            'B': {'c'}
        },
        {
            'S': {'$'},
            'A': {'b', 'c'},
            'B': {'c'},
            'C': {'$'}
        }
    ]

    def test_compute_first(self):
        for i, productions in enumerate(self.productions):
            with self.subTest(i=i):
                first = defaultdict(set)
                visited = set()
                for non_terminal in productions:
                    compute_first(non_terminal, productions, first, visited)
                self.assertEqual(first, self.expected_first[i])

    def test_compute_first_string(self):
        for i, productions in enumerate(self.productions):
            with self.subTest(i=i):
                first = defaultdict(set)
                visited = set()
                for non_terminal in productions:
                    compute_first(non_terminal, productions, first, visited)
                result = compute_first_string(['A', 'B'], productions, first)
                if i == 0:
                    self.assertEqual(result, {'a', 'b'})
                elif i == 1:
                    self.assertEqual(result, {'a', 'd'})
                elif i == 2:
                    self.assertEqual(result, {'a', 'b', 'e'})

    def test_compute_follow(self):
        for i, productions in enumerate(self.productions):
            with self.subTest(i=i):
                first = defaultdict(set)
                follow = defaultdict(set)
                visited = set()
                for non_terminal in productions:
                    compute_first(non_terminal, productions, first, visited)
                for non_terminal in productions:
                    compute_follow(non_terminal, productions, first, follow, 'S')
                self.assertEqual(follow, self.expected_follow[i])

if __name__ == '__main__':
    unittest.main()
