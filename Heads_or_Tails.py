import random

x = int(input('Number of flips: '))
if x < 0:
	x = str(x)[1:]
	x = int(x)
Heads = 0

for n in range(1, x + 1):
	roll = random.randrange(2)
	if roll == 1:
		Heads += 1


print('Number of Heads: ' + str(Heads))
print('Number of Tails: ' + str(x - Heads))