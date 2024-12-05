# cat sample_input | egrep -o 'mul\([0-9]{1,3},[0-9]{1,3}\)'

import re

matches = []

with open('input', 'r') as f:
	for line in f.readlines():
		# part 1
		# matches += re.findall('mul\([0-9]{1,3},[0-9]{1,3}\), line)
		# part 2
		matches += re.findall('mul\([0-9]{1,3},[0-9]{1,3}\)|do\(\)|don\'t\(\)', line)

sum = 0

PROCESS_INPUT = True

for match in matches:
	print(match)
	if match == "don't()":
		PROCESS_INPUT = False
		continue

	if match == "do()":
		PROCESS_INPUT = True
		continue

	if PROCESS_INPUT:
		arg1 = int(match.split(",")[0].split("(")[1])
		arg2 = int(match.split(",")[1].replace(")", ""))
		sum += (arg1 * arg2)

print(len(matches))
print(sum)

