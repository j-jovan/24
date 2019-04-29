# 'Make 24' game
# Inspired by the code I saw on some website
# Goal of the game is to make the number 24 using all provided digits
# Q quits the game, N gives new numbers
# 'En' selects English version, 'Sr' selects Serbian version of the game

import random


def choose4(): # Return 4 random digits
    return [str(random.randint(1,9)) for i in range(4)]

def numbers(numbers1):
	print("Numbers are "+ "".join(numbers1))

def main():
	numbers1 = choose4()
	numbers(numbers1)

if __name__ == '__main__': main() # Set main() as start funct