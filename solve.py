#!/usr/bin/python

import socket
import time
import re
import commands
import sys,time,string

move = [["","r","","d"],
	["l","","r","","d"],
	["","l","","","","d"],
	["u","","","","r","","d"],
	["","u","","l","","r","","d"],
	["","","u","","l","","","","d"],
	["","","","u","","","","r"],
	["","","","","u","","l","","r"],
	["","","","","","u","","l"]]
 
ADDRESS = "203.178.135.99"
PORT = 12001

s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((ADDRESS, PORT))
 
# fetch data
data = s.recv(2048)
print data
data = s.recv(2048)
print data
while True:
	print data
	data = data.split("\n")
	print data
	for i in range(0,len(data)):
		if data[i].startswith("Problem"):
			break
	print i
	puzzle = []
	puzzle.append(data[i+2].split("|"))
	puzzle.append(data[i+3].split("|"))
	puzzle.append(data[i+4].split("|"))
	print puzzle

	command = "./solve_puzzle.py %s %s %s %s %s %s %s %s %s" % (puzzle[0][1], puzzle[0][2], puzzle[0][3], puzzle[1][1], puzzle[1][2], puzzle[1][3], puzzle[2][1], puzzle[2][2], "0")
	print command
	command_list = commands.getoutput(command)
	command_list = command_list.split("\n")
	print command_list
	space_index = []
	for command in command_list:
		command = command.strip("[]")
		command = command.translate(string.maketrans("", ""), " ") 
		command = command.split(",")
		if len(command) == 9:
			space_index.append(command.index("0"))
	print space_index
	answer = []
	for i in range(1,len(space_index)):
#		print "before:%d after:%d" %(space_index[i - 1], space_index[i])
		answer.append(move[space_index[i - 1]][space_index[i]])
	
	for command in answer:
		command += "\n"
		s.send(command) 
		data = s.recv(2048)
		print data	 

