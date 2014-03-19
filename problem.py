#! /usr/bin/python

from copy import deepcopy
from puzzle import Puzzle
import sys,time

# define question array
p = Puzzle([
		["1","2","3"],
		["4","5","6"],
		["7","8"," "],

	]) 

# define goal array
goal = Puzzle(deepcopy(p.Array))
# define where there is a space
space_index = [2,2] 

def check_answer():
	""" Check the answer is correct """
	if p.Array == goal.Array:
		print "Clear!!"
		return True		
	else:
		return False

def print_problem(puzzle):
	""" print problem statement """
	print "\nProblem %d" % (i)
	puzzle.print_puzzle()

	# flush stdout
	sys.stdout.flush()

def move_space(horizontal, positive):
	""" move space """
	global p, space_index 

	# horizontal or vertical ?
	is_horizontal = 1 if horizontal else 0
	# define dead_end
	dead_end = 2 if positive else 0
	# If dead end, return
	if space_index[is_horizontal] == dead_end: 
		print "Invalid"
		return 

	# whether the positive direction in array index
	direction = 1 if positive else -1

	if horizontal:
		p.swap(space_index[0], space_index[1], space_index[0], space_index[1] + direction)
	else:
		p.swap(space_index[0], space_index[1], space_index[0] + direction, space_index[1] )
	space_index[is_horizontal] = space_index[is_horizontal] + direction

def problem():
	""" Question """
	# declare variables
	global p, goal

	# shuffle p (create problem)
	p.shuffle(i * 2)

	print_problem(p)

	while True:
		# read from stdin
	        s = sys.stdin.readline()
		# delete blank character
		s = s.rstrip()

		# switch by the entered character
		if s == 'exit': # exit this program
			return False
	 	# blank moves left 
		elif s == 'l':
			move_space(horizontal = True, positive = False)
		# blank moves right
		elif s == 'r': 
			move_space(horizontal = True, positive = True)
		# blank moves up
		elif s == 'u': 
			move_space(horizontal = False, positive = False)
		# blank moves down
		elif s == 'd': 
			move_space(horizontal = False, positive = True)
		# invalid input
		else:
			print "r:right l:left u:up d:down\n"

		# show current puzzle
		p.print_puzzle()

		# return true if the answer is correct
		if check_answer(): 
			return True

		# flush stdout
		sys.stdout.flush()
	

if __name__ == "__main__":

	# print problem statement
	print "\nSolve the 8-Puzzle!!\nr:right l:left u:up d:down\n"
	print "Goal"
	p.print_puzzle()
	
	# flush stdout
	sys.stdout.flush()
	
	# record the start time
	starttime = time.time()

	# question 50 questions
	for i in range(1,50):
		# culculate processing time
		current = int(time.time() - starttime)
		
		# if it is too slow, program exit
		if current > 20:
			print "too slow..."
			sys.exit()

		if problem():
			continue
		else:
			print "see you..."
			sys.exit()
	
	# print answer
	print "flag:8puzzle is fun!!"		
	sys.exit()
