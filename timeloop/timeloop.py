#!/bin/python2
import sys

def read_input():
	data = int(sys.stdin.read())
	return data

def problem():
	data = read_input()
	for i in range(1, data+1):
		print i, "Abracadabra"

problem()