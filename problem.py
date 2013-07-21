#! /usr/bin/python

from copy import deepcopy
from puzzle import Puzzle
import sys

def check_answer():
	if p.Array == answer.Array:
		print "Clear!!"
		return True		
	else:
		return False

#define question array
p = Puzzle([
		["1","2","3"],
		["4","5","6"],
		["7","8"," "],

	]) 

answer = Puzzle(deepcopy(p.Array))

print "\nSolve the 8-Puzzle!!\nr:right l:left u:up d:down\n"
print "Goal"
p.print_puzzle()

p.shuffle(2)
print "\nProblem"
p.print_puzzle()
#p.swap(0,0,0,1)
#p.print_puzzle()
sys.stdout.flush()

#for line in sys.stdin:
#    print "test" 
while True:
        s = sys.stdin.readline()
	s = s.rstrip()
	if s == 'exit':
		break
	elif s == 'l':
		if space_index[1] == 0:
			print "Invalid"
		else:
			p.swap(space_index[0],space_index[1],space_index[0],space_index[1]-1)
			space_index[1] -= 1
	elif s == 'r':
		if space_index[1] == 2:
			print "Invalid"
		else:
			p.swap(space_index[0],space_index[1],space_index[0],space_index[1]+1)
			space_index[1] += 1
	elif s == 'u':
		if space_index[0] == 0:
			print "Invalid"
		else:
			p.swap(space_index[0],space_index[1],space_index[0] - 1, space_index[1])
			space_index[0] -= 1
	elif s == 'd':
		if space_index[0] == 2:
			print "Invalid"
		else:
			p.swap(space_index[0],space_index[1],space_index[0] + 1, space_index[1])
			space_index[0] += 1
#        print s
	p.print_puzzle()
	if check_answer(): 
		print "flag:testtest"
		break
	sys.stdout.flush()

