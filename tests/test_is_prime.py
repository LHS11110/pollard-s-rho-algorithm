import unittest
from src.pollard_rho import is_prime

class TestIsPrime(unittest.TestCase):
    def test_small_primes(self):
        # Bases used are 2, 3, 5, 7, 11, 13, 17
        # Ensure these pass (some might fail with current implementation)
        primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31]
        for p in primes:
            with self.subTest(p=p):
                self.assertTrue(is_prime(p), f"{p} should be prime")

    def test_small_composites(self):
        composites = [4, 6, 8, 9, 10, 12, 14, 15, 16, 18, 20, 21, 22, 24, 25, 27]
        for c in composites:
            with self.subTest(c=c):
                self.assertFalse(is_prime(c), f"{c} should be composite")

    def test_known_failures_in_naive_impl(self):
        # Carmichael numbers or strong pseudoprimes if bases were fewer
        # With current bases [2, 3, 5, 7, 11, 13, 17], these should be correctly identified as composite
        carmichaels = [561, 1105, 1729, 2465, 2821, 6601, 8911]
        for c in carmichaels:
            with self.subTest(c=c):
                self.assertFalse(is_prime(c), f"{c} is a Carmichael number (composite)")

    def test_large_primes(self):
        # Mersenne primes and others
        large_primes = [
            2**19 - 1, # 524287
            2**31 - 1, # 2147483647
            # A prime near 2^62
            # 2^62 = 4611686018427387904
            # Next prime after 2^60 might be good enough to test "large" range
            1152921504606846976 + 39, # A prime near 2^60
            # Let's use a known 64-bit prime
            18446744073709551557 # Largest 64-bit prime (unsigned), but python handles arbitrary int
        ]
        # Wait, the user said "2^62 이하" (<= 2^62). 
        # 18446744073709551557 is > 2^62 (approx 4.6e18). 
        # 2^64 approx 1.8e19.
        # Let's pick a prime slightly less than 2^62.
        # 2^62 - 1 is not prime (div by 3).
        # Let's verify a few large primes within range.
        large_primes_in_range = [
            4611686018427387847, # Prime < 2^62
        ]
        
        for p in large_primes_in_range:
            with self.subTest(p=p):
                self.assertTrue(is_prime(p), f"{p} should be prime")

    def test_large_composites(self):
        # A composite near 2^62
        # product of two large 31-bit primes
        p1 = 2147483647 # 2^31 - 1
        p2 = 2147483629 # Another prime
        comp = p1 * p2
        # This is approx 4.6e18, near 2^62
        self.assertFalse(is_prime(comp), f"{comp} should be composite")

if __name__ == '__main__':
    unittest.main()
