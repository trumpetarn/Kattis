import sys

input_data = sys.stdin.read().split('\n')
if len(input_data[0])<len(input_data[1]):
	print "no"
else:
	print "go"
sys.exit(0)