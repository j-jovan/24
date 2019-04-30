# 'Make 24' game
# Inspired by the code I saw on some website
# Goal of the game is to make the number 24 using all provided number
# Q quits the game, N gives new numbers
# 'En' selects English version, 'Sr' selects Serbian version of the game

from __future__ import division, print_function
import random, ast, re
import sys

def choose4(): # Return 4 random number
    return [str(random.randint(1,9)) for i in range(4)]

def numbers(number):
	print("Numbers are "+ "".join(number))

def check(solution, number):
    allowed = set('() +-*/\t'+''.join(number))
    ok = all(ch in allowed for ch in solution) and \
         all(number.count(dig) == solution.count(dig) for dig in set(number)) \
         and not re.search('\d\d', solution)
    if ok:
        try:
            ast.parse(solution)
        except:
            ok = False
    return ok

def main():
	number = choose4()
	numbers(number)
	solution = ''
	provera = solution = False
	
	#solution = input(%i)

if __name__ == '__main__': main() # Set main() as start funct