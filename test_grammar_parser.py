import unittest
from main import compute_first_and_follow_sets

class TestGrammarParser(unittest.TestCase):
    def read_grammar(self, filename):
        with open(filename, 'r') as file:
            return file.read()
    
    def test_grammar_1(self):
        grammar = self.read_grammar('grammars/grammar1.txt')
        first, follow = compute_first_and_follow_sets(grammar)
        self.assertEqual(first['S'], {'a', 'b', 'e'})
        self.assertEqual(follow['S'], {'$'})
        self.assertEqual(first['A'], {'a', 'e'})
        self.assertEqual(follow['A'], {'b'})
        self.assertEqual(first['B'], {'b'})
        self.assertEqual(follow['B'], {'$', 'a'})

    def test_grammar_2(self):
        grammar = self.read_grammar('grammars/grammar2.txt')
        first, follow = compute_first_and_follow_sets(grammar)
        self.assertEqual(first['S'], {'a', 'd', 'b', 'c', 'e'})
        self.assertEqual(follow['S'], {'$'})
        self.assertEqual(first['A'], {'a', 'e'})
        self.assertEqual(follow['A'], {'b'})
        self.assertEqual(first['B'], {'d'})
        self.assertEqual(follow['B'], {'c'})
    
    def test_grammar_3(self):
        grammar = self.read_grammar('grammars/grammar3.txt')
        first, follow = compute_first_and_follow_sets(grammar)
        self.assertEqual(first['S'], {'a', 'b', 'c', 'e'})
        self.assertEqual(follow['S'], {'$'})
        self.assertEqual(first['A'], {'a', 'e'})
        self.assertEqual(follow['A'], {'b', 'c'})
        self.assertEqual(first['B'], {'b', 'e'})
        self.assertEqual(follow['B'], {'c'})
        self.assertEqual(first['C'], {'c'})
        self.assertEqual(follow['C'], {'$', 'a'})

if __name__ == '__main__':
    unittest.main()
