#!/bin/python2
import sys

def read_input():
	data = sys.stdin.read().split('\n')
	return data

def problem():
	data = read_input()
	numbers = [ int(x) for x in data[0].split(' ') ]
	numbers = sorted(numbers)
	A = numbers[0]
	B = numbers[1]
	C = numbers[2]
	string = data[1].replace('A', str(A)+' ')
	string = string.replace('B', str(B)+' ')
	string = string.replace('C', str(C)+' ')
	print string[:-1]

problem()