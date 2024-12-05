levels = []

# First, I want to turn everything into a list of ints. 
with open('input', 'r') as f:
	for line in f.readlines():
		# There's probably an easier way to do this with map() or a list comprehension. 
		level = line.split(" ")
		for i in range(0, len(level)):
			level[i] = int(level[i])
		levels.append(level)

def level_is_increasing(level):
	for i in range(0, len(level)):
		if i == 0:
			continue
		if level[i] <= level[i - 1]:
			return False
	return True

def level_is_decreasing(level):
	for i in range(0, len(level)):
		if i == 0:
			continue
		if level[i] >= level[i - 1]:
			return False
	return True

def level_safe_intervals(level):
	for i in range(0, len(level)):
		if i == 0:
			continue
		if abs(level[i] - level[i - 1]) > 3:
			return False
	return True

def level_is_safe(level):
	if (not level_is_increasing(level)) and (not level_is_decreasing(level)):
		return False

	if not level_safe_intervals(level):
		return False

	return True

safe = 0
unsafe = 0

# part 1
for level in levels:
	if level_is_safe(level):
		safe += 1
	else:
		unsafe += 1

print(safe)

# If a level is sent here, assume it's already been deemed unsafe. 
def problem_dampener(level):
	# For each index, try removing one and see if it's safe. 
	for i in range(0, len(level)):

		# tmp_lvl = level causes level to be affected by methods that
		# we apply to tmp_lvl. So we need to explicitly make a copy.
		tmp_lvl = level.copy()
		del tmp_lvl[i]

		if(level_is_safe(tmp_lvl)):
			return True
	return False

safe = 0
unsafe = 0

for level in levels:
	if(
		(level_is_increasing(level) or level_is_decreasing(level))
		and
		(level_safe_intervals(level))
	):
		safe += 1
	else:
		if(problem_dampener(level)):
			safe += 1
		else:
			unsafe += 1

print(safe)
