from datetime import datetime

def sieve_of_eratosthenes(limit):
    primes = [True] * (limit + 1)
    p = 2
    while p * p <= limit:
        if primes[p]:
            for i in range(p * p, limit + 1, p):
                primes[i] = False
        p += 1
    prime_numbers = [p for p in range(2, limit) if primes[p]]
    return prime_numbers

# Estimate the upper limit to find the first 100000 prime numbers
# Using the approximation: n * log(n) + n * log(log(n))
# For n = 100000, the upper limit is around 1,300,000
start = datetime.now()
upper_limit = 15500000
primes = sieve_of_eratosthenes(upper_limit)

# Extract the first 100000 primes
first_1000000_primes = primes[:1000000]

print("The first 100000 prime numbers are: ")
for index, prime in enumerate(first_1000000_primes):
    print(f"Prime {index+1} is {prime}")

end = datetime.now()
print(f"It took {end-start}")