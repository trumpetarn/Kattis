#!/bin/python2
import sys

def read_input():
	data = sys.stdin.read().split('\n')
	return data

def problem():
	data = read_input()
	num_cases = int(data[0])
	for i in range(1,num_cases+1):
		line =  data[i].split(' ')
		b = int(line[0])
		p = float(line[1])
		BPM = 60*b/p
		t_min = p/(b+1)
		t_max = p/(b-1)
		ABPM_min = 60/t_max
		ABPM_max = 60/t_min
		print "%.4f %.4f %.4f" % (ABPM_min,BPM,ABPM_max)

problem()