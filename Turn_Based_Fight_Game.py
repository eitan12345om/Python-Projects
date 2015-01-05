import random
import time

def attacking(attack, health):
	for hitpoints in range(attack):
		if health > 0:
			health -= 1
	return health

def healing(heal, health):
	for hitpoints in range(heal):
		if health < 100:
			health += 1
	return health

menu = {}
menu['1.'] = "Moderate Attack (18-25)" 
menu['2.'] = "Heavy Attack (10-35) with (0-5) recoil"
menu['3.'] = "Heal (18-25)"
menu['4.'] = "Poison Blade: Will add an extra 5 damage every turn."

Human_Health = 100
Computer_Health = 100
moves = ['moderate', 'heal']
moves2 = ['moderate', 'moderate', 'heal', 'heal', 'heal', 'heal', 'heal', 'heal', 'heal', 'heal']
Blade_poisoned = False


print('Your health:', str(Human_Health) + '     ' + 'Computer health:', str(Computer_Health))
while Human_Health > 0 and Computer_Health > 0:

	Move = False
	while Move == False:
		print('\n' + 'Moves available:')
		options = list(menu.keys())
		options.sort()
		if Blade_poisoned == False:
			for entry in options:
				print(entry, menu[entry])
		else:
			for entry in options[0:3]:
				print(entry, menu[entry])

		print('\n')
		Selection = input("Select your move: ")
		print('\n')
		if not Selection.isnumeric():
			print("Unknown Option Selected!")
			print('Your health:', str(Human_Health) + '     ' + 'Computer health:', str(Computer_Health) + '\n')
		else:
			Selection = int(Selection)
			Move = True
			if Selection == 1:
				attack = random.randrange(18, 26)
				Computer_Health = attacking(attack, Computer_Health)
				if Blade_poisoned == True:
					Computer_Health = attacking(5, Computer_Health)
					print("You've dealt", str(attack), "damage (+5 poison damage), a total damage of:", str(attack +5))
				else:
					print("You've dealt", str(attack), "damage")
			elif Selection == 2:
				attack = random.randrange(10, 36)
				recoil = random.randrange(0, 6)
				Computer_Health = attacking(attack, Computer_Health)
				Human_Health = attacking(recoil, Human_Health)
				if Blade_poisoned == True:
					Computer_Health = attacking(5, Computer_Health)
					print("You've dealt", str(attack), "damage (+5 poison damage), a total damage of:", str(attack +5))
				else:
					print("You've dealt", str(attack), "damage")
				print("Your weapon recoils and hits you for:", str(recoil), "lifepoint(s)")
			elif Selection == 3:
				heal = random.randrange(18, 26)
				Human_Health = healing(heal, Human_Health)
				print("You've been healed", str(heal), 'life points!')
			else:
				Blade_poisoned = True
				print("You've poisoned your blade!")

	if Computer_Health > 0:			
		print('Your health:', str(Human_Health) + '     ' + 'Computer health:', str(Computer_Health) + '\n')			
	time.sleep(1)

	if Computer_Health > 0:
		if Computer_Health > 60 or Human_Health < 30:
			Computer_move = 'moderate'
		elif Computer_Health < 20:
			Computer_move = 'heal'
		elif Computer_Health < 30:
			Computer_move = random.choice(moves2)
		else:
			Computer_move = random.choice(moves)
		if Computer_move == 'heal':
			heal = random.randrange(18, 26)
			Computer_Health = healing(heal, Computer_Health)
			print("The Computer healed", str(heal), 'life points!')
		else:
			if Computer_move == 'moderate':
				attack = random.randrange(18, 26)
			else:
				attack = random.randrange(10, 31)
			Human_Health = attacking(attack, Human_Health)
			print("You've been dealt a blow of", str(attack))

	print('Your health:', str(Human_Health) + '     ' + 'Computer health:', str(Computer_Health))
	time.sleep(2)

if Computer_Health == Human_Health:
	print('You both died!')
elif Computer_Health == 0:
	print('You Win!')
else:
	print('You Lose!')