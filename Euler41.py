#Pandigital prime
#Problem 41
#We shall say that an n-digit number is pandigital if it makes use of all the digits 1 to n exactly once. For example,
# 2143 is a 4-digit pandigital and is also prime.
#
#What is the largest n-digit pandigital prime that exists?

import string, itertools



#pan_nums = itertools.permutations(string.digits.replace('0', ''))

p_strs = []
for p in itertools.permutations('123456789'):
    p_str = ''
    for q in p:
        p_str += q
    p_strs.append(p_str)

limit = int(max(p_strs))
def sieve_of_eratosthenes():
    is_prime = [True for i in range(limit + 1)]
    for n in range(2, limit + 1):
        if is_prime[n]:
            #strike all multiples of n
            m = 2 * n
            while m <= limit:
                is_prime[m] = False
                m += n
    return is_prime

is_prime = sieve_of_eratosthenes()

for p in reversed(p_strs):
    if is_prime[int(p)]:
        print(p)
        break