import random

top_range = input("Type a number: ")

if top_range.isdigit():
	top_range=int(top_range)

	if top_range <= 0:
		print("Enter a number greater than zero next time")
		exit()
else:
	print("Enter a valid number next time")
	quit()

num = random.randrange(top_range)
print("Computer has choosen a number between 0 to " + str(top_range) + ". Guess the number. You get to guess 3 times")

for i in range(3):
	guess = input("\nEnter your guess: ")
	if guess.isdigit():
		guess = int(guess)
	else:
		print("Guess can only be a number. Try again")
		continue

	if guess == num:
		print("🎉 Hurray!! 🎉 You got it correct")
		break

	elif guess > num:
		print("Your guess is greater than the actual number, Try again.")
		print("Guesses left: " + str(2-i))

	else: 
		print("Your guess is less than the actual number, Try again.")
		print("Guesses left: " + str(2-i))
		
if guess != num:
	print("You lose!! 🙁 Try again")
