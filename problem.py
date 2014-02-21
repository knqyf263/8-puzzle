#! /usr/bin/python

from copy import deepcopy
from puzzle import Puzzle
import sys,time

def check_answer():
	if p.Array == default.Array:
		print "Clear!!"
		return True		
	else:
		return False

def problem():
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
		else:
			print "r:right l:left u:up d:down\n"
	#        print s
		p.print_puzzle()
		if check_answer(): 
			return True
			break
		sys.stdout.flush()
	
#define question array
p = Puzzle([
		["1","2","3"],
		["4","5","6"],
		["7","8"," "],

	]) 

space_index = [2,2]
default = Puzzle(deepcopy(p.Array))

print "\nSolve the 8-Puzzle!!\nr:right l:left u:up d:down\n"
print "Goal"
p.print_puzzle()

sys.stdout.flush()

starttime = time.time()
for i in range(2,50):
	current = int(time.time() - starttime)
	if current > 20:
		print "too slow..."
		sys.exit()
	p.Array = deepcopy(default.Array)
	p.shuffle(i * 2)
	print "\nProblem %d" % (i - 1)
	p.print_puzzle()
	sys.stdout.flush()
	if problem():
		continue

print "flag:8puzzle is fun!!"		
sys.exit()
