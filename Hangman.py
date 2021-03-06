# This program can b used to play hangman
import random

def replace(word, character, index):
	try:
		return word[:index] + character + word[index + 1:]
	except IndexError:
		return word[:index] + character

Play_again, Wins, Losses = 'y', 0, 0
words = ['jazz', 'refrigerator', 'beautiful', 'rhythm', 'bookworm', 'croquet', 'knapsack', 'mystify', 'glowworm', 'numbskull', 'oxygen', 'pizazz', 'rhubarb', 'pixel', 'unknown', 'zombie', 'vortex']

while Play_again == 'y':
	alphabet = 'abcdefghijklmnopqrstuvwxyz'
	word = random.choice(words)
	words.remove(word)
	Guessed_word = '_' * len(word)
	Lives, Win = 7, 0

	while Lives > 0 and Win == 0:
		
		Valid_Guess = False
		while Valid_Guess == False:
			print('\n' + Guessed_word, '(' + str(len(word)) + ' characters long)')
			print('Available letters to guess:', alphabet)
			
			if Lives != 1:
				print('You have', Lives, 'lives left')
			else:
				print('You have', Lives, 'life left')
			
			guess = input('Guess one character: ')
			guess = guess.lower()
			if guess in alphabet:
				Valid_Guess = True
			elif len(guess) > 1:
				print('Must be 1 character!')
			elif guess.isalpha():
				print('You already guessed this letter!')
			else:
				print('Must be a letter!')
		
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
			Win = 1
			print('\n' + word)

	if Win == 1:
		Wins += 1
		print('\n' + 'You Win!')
	else:
		Losses += 1
		print('\n' + 'You Lose!' + '(' + str(Wins) + ' wins/' + str(Losses) + ' losses)')
		print('The word was:', word)
	
	if Wins == 1:
		Win_Loss_Count = '(' + str(Wins) + ' win'
	else:
		Win_Loss_Count = '(' + str(Wins) + ' wins'
	if Losses == 1:
		print(Win_Loss_Count + '/' + str(Losses) + ' loss)')
	else:
		print(Win_Loss_Count + '/' + str(Losses) + ' losses)')

	if words:
		while Valid_Guess == True:
			print('\n')
			Play_again = input('Do you want to play again (y/n)? ')
			Play_again = Play_again.lower()
			if Play_again == 'y':
				print('Good luck!')
				Valid_Guess = False
			elif Play_again == 'n':
				print('See you next time!')
				Valid_Guess = False
			else:
				print("Please enter either 'y' or 'n'")
	else:
		print('\n' + 'Out of words!')
		print('See you next time!')
		Play_again = 'n'
