from datetime import datetime


def sieve_of_eratosthenes(limit: int) -> list:
    """Use the sieve of Eratosthenes to find all prime numbers up to a limit.
    1. Create a list of consecutive integers from 2 through n: (2, 3, ..., n).
    2. Let p equal 2, the first prime number.
    3. Starting from p, count up in increments of p and mark each of these
        numbers greater than p itself in the list.
    4. Find the first number greater than p in the list that is not marked. If
        there was no such number, stop.
    5. Otherwise, let p now equal this new number (which is the next prime),
        and repeat from step 3.
    6. When the algorithm terminates, the unmarked numbers in the list are all
        the prime numbers below n.

    Args:
        limit (int): Up to which number to find prime numbers.

    Returns:
        list: prime numbers up to the limit.
    """
    primes = []
    sieve = [True] * (limit + 1)  # Set the all number to limit to True
    sieve[0] = False  # 0 is not prime
    sieve[1] = False  # 1 is not prime
    for start in range(2, limit + 1):
        if sieve[start]:
            primes.append(start)
            for multiple in range(start * start, limit + 1, start):
                sieve[multiple] = False
    return primes


if __name__ == "__main__":
    start = datetime.now()
    n = 100000000
    primes = sieve_of_eratosthenes(n)
    primes = primes[0:1000000]
    print(primes[0:1000000])
    print(len(primes))
    end = datetime.now()
    print(f"It took {end-start}")
