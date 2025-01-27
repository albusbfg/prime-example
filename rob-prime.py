from datetime import datetime
start = datetime.now()

# Find and print the first 1,000,000 prime numbers
primes = [2]

def isprime(n):
    if n % 2 == 0:
        return False
    for prime in primes:
        if n % prime == 0:
            return False
    return True

n = 2
while len(primes) < 1000000:
    isprime(n)
    n += 1

end = datetime.now()
print(f"It took {end-start}")
