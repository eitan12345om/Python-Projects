# This converts a string into pig latin




def Piglatin(plaintext):
	vowels = ['a', 'e', 'i', 'o', 'u']
	special_cases = ['ch', 'th', 'sh', 'ph']
	words = []
	word = ''
	plaintext = plaintext.lower()
	for ch in plaintext:
		if ch != ' ':
			word += ch
		else:
			words.append(word)
			word = ''
	words.append(word)
	word = ''
	for element in words:
		if element[0] in vowels:
			pig = element + 'way'
		elif element[0:2] in special_cases:
			pig = element[2:] + element[0:2] + 'ay'
		else:
			pig = element[1:] + element[0] + 'ay'
		word = word + pig + ' '

	return word

print(Piglatin(input('Type your message here: ')))