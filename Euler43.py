#Sub-string divisibility
#Problem 43
#The number, 1406357289, is a 0 to 9 pandigital number because it is made up of each of the digits 0 to 9 in some order,
#  but it also has a rather interesting sub-string divisibility property.
#
#Let d1 be the 1st digit, d2 be the 2nd digit, and so on. In this way, we note the following:
#
#d2d3d4=406 is divisible by 2
#d3d4d5=063 is divisible by 3
#d4d5d6=635 is divisible by 5
#d5d6d7=357 is divisible by 7
#d6d7d8=572 is divisible by 11
#d7d8d9=728 is divisible by 13
#d8d9d10=289 is divisible by 17
#Find the sum of all 0 to 9 pandigital numbers with this property.

import itertools, string

p_strs = []
for p in itertools.permutations(string.digits):
    p_str = ''
    for q in p:
        p_str += q
    p_strs.append(p_str)

primes = [2, 3, 5, 7, 11, 13, 17]

def check_divisibility(n):
    divisible = True
    for i in range(len(n) - 3):
        divisible = divisible and (int(str(n[i + 1]) + str(n[i + 2]) + str(n[i + 3])) % primes[i]) == 0
    return divisible

p_sum = 0
for p in p_strs:
    if check_divisibility(p):
        print(p)
        p_sum += int(p)

print(str(p_sum))