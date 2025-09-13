# Original list of first ten prime numbers
prime_numbers = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]

# a) Extract the middle five primes
middle_five = prime_numbers[2:7]   # indices 2 to 6
print("Middle five primes:", middle_five)

# b) Get every second prime
every_second = prime_numbers[::2]  # step = 2
print("Every second prime:", every_second)

# c) Use negative indexing (last 3 primes)
last_three = prime_numbers[-3:]
print("Last three primes:", last_three)

# d) Reverse the list
reversed_list = prime_numbers[::-1]
print("Reversed list:", reversed_list)

# e) Descending Order
descending_list = sorted(prime_numbers, reverse=True)
print("Descending order:", descending_list)
