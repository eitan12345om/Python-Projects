# This program determines if a number is prime

print('This program will determine if a number is prime.')
print('\n')

a = True

while a == True:
	number = int(input('What is the number? '))
	if number < 0:
		print('Number must be positive!')
		print('\n')
	else:
		a = False

a = True
b = 0
i = 2

while a == True:
	if number == 1:
		b = 1
		a = False
	elif number == 2:
		a = False
	elif number % i == 0:
		b = 1
		a = False
	elif i >= int(number**0.5):
		a = False
	else:
		i +=1


if b == 1:
	print('No, ' + str(number) + ' is not a prime number')
else:
	print('Yes, ' + str(number) + ' is a prime number')