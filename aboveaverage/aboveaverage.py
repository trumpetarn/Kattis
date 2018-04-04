#!/bin/python2
import sys

def read_input():
	data = sys.stdin.read().split('\n')
	return data

def format_datasets(data):
	datasets = []
	for line in data:
		l = line.split(' ')
		for val in l:
			datasets.append(int(val))
	return datasets

def problem():
	data = read_input()
	num_tc = int(data[0])
	datasets = format_datasets(data[1:-1])
	i = j = 0
	while i < num_tc:
		num_people = datasets[j]
		dataset = datasets[j+1:j+num_people+1]
		average = sum(dataset)/float(num_people)
		above = 0
		for x in dataset:
			if x > average:
				above += 1
		print "{0:0.3f}%".format(100*above/float(num_people))
		j += num_people+1
		i += 1

problem()