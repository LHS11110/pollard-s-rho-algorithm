# Pollard's Rho Algorithm

This is a Python implementation of Pollard's Rho algorithm for integer factorization.

## Project Structure

- `src/`: Contains the source code.
    - `pollard_rho.py`: Implementation of `gcd`, `pollard_rho`, `factorize`, and `is_prime` (Miller-Rabin) functions.
- `tests/`: Contains unit tests.
    - `test_pollard_rho.py`: Tests for factorization algorithm.
    - `test_is_prime.py`: Tests for primality testing.

## Usage

You can use the `factorize` function to find prime factors of a number.

```python
from src.pollard_rho import factorize

number = 10403
factors = factorize(number)
print(f"Factors of {number}: {factors}")
# Output: Factors of 10403: [101, 103]
```

## Running Tests

To run the unit tests, execute the following command from the root directory:

```bash
python3 -m unittest discover tests
```

Or run specific test files:

```bash
python3 -m unittest tests/test_is_prime.py
python3 -m unittest tests/test_pollard_rho.py
```
