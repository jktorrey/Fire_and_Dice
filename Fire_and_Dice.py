#Fire & Dice
import random
from random import randint

#Welcome Statement
print ("Welcome to Fire & Dice! \nChoose how many dice to roll and how many sides they have. \nExample: a value of \'5D20\' will roll five 20-sided dice and return five values between 1 and 20 inclusive.")

#Function to roll die/dice
def dice_roll(number_dice, die_type):
	number_dice = int(number_dice)
	die_type = int(die_type)
	while number_dice >= 1:
		result_array.append(randint(1, die_type))
		number_dice = number_dice - 1
	print ("You rolled", result_array, "and your total is", sum(result_array))
	return

#Function for when a value fails
def fail():
	print ("Please try again.")
	return

#Begin main program
value = ""
array = []
while value != "EXIT":
	result_array = []
	value = input("Please enter a value or 'EXIT': ")
	value = value.upper()
	if "D" in value:
		if "DD" in value:
			fail()
		else:
			array = value.split("D")
			if (array[0] != "") and (array[1] != ""):
				number_dice = int(array[0])
				die_type = int(array[1])
				if (number_dice > 0) and (die_type > 0):
					dice_roll(number_dice, die_type)
				elif value != "EXIT":
					fail()
			elif value != "EXIT":
				fail()
	elif value != "EXIT":
		fail()
print ("Oh no, don't go!")