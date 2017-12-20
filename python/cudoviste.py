import sys

def print_result(list):
  for item in list:
    print item
  sys.exit(0)

input_data = sys.stdin.read().split('\n')
rc = input_data[0].split(' ')
rows = int(rc[0])
columns = int(rc[1])
result = [0,0,0,0,0]

if rows < 2 or columns < 2:
  print_result(result)

for row in range(1, rows):
  for column in range(0,columns-1):
    temp_parking = [input_data[row][column], input_data[row][column+1], input_data[row+1][column], input_data[row+1][column+1]]
    if not "#" in temp_parking:
      result[temp_parking.count('X')] = result[temp_parking.count('X')] + 1
print_result(result)
