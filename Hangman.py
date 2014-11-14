# This program can b used to play hangman
import random

def replace(word, character, index):
	try:
		return word[:index] + character + word[index + 1:]
	except IndexError:
		return word[:index] + character

alphabet = 'abcdefghijklmnopqrstuvwxyz'
words = ['jazz', 'refrigerator', 'beautiful', 'rhythm', 'bookworm', 'croquet', 'knapsack', 'mystify', 'glowworm', 'numbskull', 'oxygen', 'pizazz', 'rhubarb', 'pixel', 'unknown', 'zombie', 'vortex']
word = random.choice(words)
Guessed_word = '_' * len(word)
Lives = 7
a = 0

while Lives > 0 and a == 0:
	
	Valid_Guess = False
	while Valid_Guess == False:
		print('\n' + Guessed_word, '(' + str(len(word)) + ' characters long)')
		print('Available letters to guess:', alphabet)
		
		if Lives != 1:
			print('You have', Lives, 'lives left')
		else:
			print('You have', Lives, 'life left')
		
		guess = input('Guess one character: ')
		if guess.isalpha():
			guess = guess.lower()
		if guess in alphabet:
			Valid_Guess = True
		else:
			print('Oops! Invalid Guess!')
	
	if guess in word:
		index = 0
		for ch in word:
			if guess == ch:
				Guessed_word = replace(Guessed_word, guess, index)
			index += 1
		print('\n' + 'Hooray! You guessed a correct letter!')
	else:
		if Lives != 1:
			print('\n' + 'Try Again!')
		Lives -= 1
	
	alphabet = alphabet.replace(guess, '')
	if Guessed_word == word:
		a = 1
		print('\n' + word)

if a == 1:
	print('\n' + 'You Win!')
else:
	print('\n' + 'You Lose!')
	print('The word was:', word)

