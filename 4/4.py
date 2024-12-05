puzzle = []

with open('sample_input', 'r') as f:
	for line in f.readlines():
		puzzle.append(line.replace("\n", ""))

def find_horizontal_xmas(puzzle):
	count = 0
	for line in puzzle:
		for x in range(0, len(line)):
			# If we're past the point where we can find a horiontal XMAS, skip. 
			if x > len(line) - 3:
				continue

			# Forwards
			if line[x] == "X":
				if line[x + 1] == "M":
					if line[x + 2] == "A":
						if line[x + 3] == "S":
							count += 1
			# Backwards
			if line[x] == "S":
				if line[x + 1] == "A":
					if line[x + 2] == "M":
						if line[x + 3] == "X":
							count += 1

	return count 

def find_vertical_xmas(puzzle):
	count = 0
	for x in range(0, len(puzzle)):
		for y in range(0, len(puzzle[x])):
			if y > len(puzzle[x]) - 3:
				continue

			# Downwards
			if puzzle[x][y] == "X":
				if puzzle[x][y + 1] == "M":
					if puzzle[x][y + 2] == "A":
						if puzzle[x][y + 3] == "S":
							count += 1

			# Upwards
			if puzzle[x][y] == "S":
				if puzzle[x][y + 1] == "A":
					if puzzle[x][y + 2] == "M":
						if puzzle[x][y + 3] == "X":
							count += 1

	return count

# TODO: How to handle diagonals? Separate functions for up/left up/right down/left down/right?

total_count = 0
total_count += find_horizontal_xmas(puzzle)
total_count += find_vertical_xmas(puzzle)

print(total_count)
