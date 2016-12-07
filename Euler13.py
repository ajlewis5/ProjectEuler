#Large sum
#Problem 13
#Work out the first ten digits of the sum of the following one-hundred 50-digit numbers:
#large_sum.txt

f = open('large_sum.txt','r')
lines = f.readlines()
f.close()

sum = 0
for line in lines:
    sum += int(line)

print(str(sum)[:10])