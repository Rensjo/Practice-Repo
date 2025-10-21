"""
Demonstrate the basics of parallel programming in Python using the
multiprocessing module.

This script runs a simple CPU-bound task sequentially and in parallel
so you can compare the difference.
"""

import math
import time
from multiprocessing import Pool, cpu_count


def is_prime(n: int) -> bool:
    """Return True if n is a prime number."""
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True


def count_primes_sequential(limit: int) -> int:
    """Count prime numbers up to 'limit' sequentially."""
    return sum(1 for x in range(limit) if is_prime(x))


def count_primes_parallel(limit: int) -> int:
    """Count prime numbers up to 'limit' in parallel using a process pool."""
    with Pool(processes=cpu_count()) as pool:
        results = pool.map(is_prime, range(limit))
    return sum(results)


def main() -> None:
    limit = 100_000

    start = time.time()
    sequential_count = count_primes_sequential(limit)
    seq_time = time.time() - start
    print(f"Sequential count: {sequential_count} in {seq_time:.2f}s")

    start = time.time()
    parallel_count = count_primes_parallel(limit)
    par_time = time.time() - start
    print(f"Parallel count:   {parallel_count} in {par_time:.2f}s")

    print("")
    print(
        "Parallel programming allows you to split tasks among multiple cores "
        "or processors to finish faster, as shown by the potential speed-up."
    )


if __name__ == "__main__":
    main()
