import random


print("\r\n" + "Hello, I am thinking of a number between 1 and 10 (inclusive)")

correct = False
guesses = 0
rand_num = random.randrange(1,11)

while correct == False or guesses < 3:
    guess = int(input('Guess the Number: '))
    guesses += 1
    if guess > rand_num:
        print("Guess Lower!")
    elif guess < rand_num:
    	print("Guess Higher!")
    if guess == rand_num:
    	correct = True
    print("\r\n")

print("You got it!")
print("Next level:" + "\r\n")

rand_num = random.randrange(1,101)
correct = False

print("Now, guess a number between 1 and 100")

while(correct == False):
    guess = int(input('Guess the Number: '))
    guesses = guesses + 1
    if guess > rand_num:
        print("Too High!")
    if guess < rand_num:
    	print("Too Low!")
    if guess == rand_num:
    	correct = True
    print("\r\n")


print("------You Win!------")
print("With only %s guesses" % (guesses))







