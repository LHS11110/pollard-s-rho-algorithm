import unittest
from src.pollard_rho import pollard_rho, factorize

class TestPollardRho(unittest.TestCase):
    
    def test_small_composites(self):
        self.assertIn(pollard_rho(15), [3, 5])
        self.assertIn(pollard_rho(21), [3, 7])
        self.assertIn(pollard_rho(33), [3, 11])
        
    def test_factorize_simple(self):
        self.assertEqual(factorize(15), [3, 5])
        self.assertEqual(factorize(12), [2, 2, 3])
        self.assertEqual(factorize(100), [2, 2, 5, 5])
        
    def test_prime(self):
        self.assertEqual(factorize(13), [13])
        self.assertEqual(factorize(17), [17])
        self.assertEqual(factorize(2), [2])
        
    def test_larger_numbers(self):
        # 8051 = 83 * 97
        self.assertEqual(factorize(8051), [83, 97])
        # 10403 = 101 * 103
        self.assertEqual(factorize(10403), [101, 103])
        
    def test_edge_cases(self):
        self.assertEqual(factorize(1), [])

if __name__ == '__main__':
    unittest.main()
