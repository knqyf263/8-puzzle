#! /usr/bin/python

from copy import deepcopy
import sys
import random

class Puzzle:

	def __init__(self, Array):
		self.Array = Array 

	def print_puzzle(self):
		write = sys.stdout.write
		print("+-----+")
		for i in range(0,3):	
			for j in range(0,3):	
				write("|")
				write(self.Array[i][j])
			print "|"
		print("+-----+")

	def swap(self,column1,row1,column2,row2):
		self.Array[column1][row1], self.Array[column2][row2] = 	self.Array[column2][row2], self.Array[column1][row1]

	def shuffle(self, num):
		for i in range(0, num):
			while True:
				src = self.random_array()
				dist = self.random_array()
				if src != dist:
					self.swap(src[0], src[1], dist[0], dist[1])
					break
	
	def random_array(self):
		while True:
			array = [random.randint(0,2), random.randint(0,2)]
			if array != [2,2]:
				return array

	def where_space(self):
	        for i in range(0,3):
			try:
                        	j = self.Array[i].index(" ")
                        	return [i,j]
                	except ValueError:            
                       		continue
