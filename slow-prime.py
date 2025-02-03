from datetime import datetime
start = datetime.now()
prime_numbers = [2,3]
print(f"Prime 1 is 2")
print(f"Prime 2 is 3")
limit = 1000000
index = 3
next = 5
while index < limit:
    is_prime = True
    i = 1
    while prime_numbers[i]*prime_numbers[i] <= next and is_prime:
        if next % prime_numbers[i] == 0:
            is_prime = False
        i += 1
    if is_prime:
        prime_numbers.append(next)
        print(f"Prime {index} is {next}")
        index += 1
    next += 2

print("The first 100000 prime numbers are: ")
for index, prime in enumerate(prime_numbers):
    print(f"Prime {index+1} is {prime}")

end = datetime.now()
print(f"It took {end-start}")