from math import sqrt
from typing import Tuple

N = 100000
PRIME = [True for _ in range(N + 1)]


class Solution:
    def __init__(self):
        self.solve()

    def sieve_of_eratosthenes(self) -> None:
        """
        Precalculate N first prime numbers using sieve of eratosthenes

        Time complexity: O(n*log(log(n)))
        """
        p = 2
        while p * p <= N:
            if PRIME[p]:
                for i in range(p * p, N + 1, p):
                    PRIME[i] = False
            p += 1

    def find_two_primes(self, n: int) -> Tuple[int, int]:
        """
        Given n finds two prime numbers a and b such that n = a * b

        Complexity: O(srqt(n))
        """
        a, b = None, None
        for i in range(2, int(sqrt(n))):
            if PRIME[i] and n % i == 0:
                a = i
                b = int(n / a)
        assert a is not None
        assert b is not None
        assert a * b == n
        return a, b

    def solve(self) -> None:
        """
        Handles user input
        """
        self.sieve_of_eratosthenes()
        p = int(input())

        while p > 0:
            k = int(input())

            a, b = self.find_two_primes(n=k)
            print(a, b)

            p -= 1


Solution()
