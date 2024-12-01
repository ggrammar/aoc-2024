left_list = []
right_list = []

with open('input', 'r') as f:
	for line in f.readlines():
		left_list.append(int(line.split(" ")[0]))
		right_list.append(int(line.split(" ")[3].replace("\n", "")))

def get_distance_and_remove_from_list(left, right):
	left_index = left.index(min(left))
	right_index = right.index(min(right))

	retval = abs(left[left_index] - right[right_index])

	left.pop(left_index)
	right.pop(right_index)

	return retval

total_distance = 0
		
for item in range(0, len(left_list)):
	total_distance += (get_distance_and_remove_from_list(left_list, right_list))

print(total_distance)

# Re-read input, since we destroyed it all for the first pass.
with open('input', 'r') as f:
	for line in f.readlines():
		left_list.append(int(line.split(" ")[0]))
		right_list.append(int(line.split(" ")[3].replace("\n", "")))


def get_similarity_score(int, list):
	matches = [i for i, x in enumerate(list) if x == int]
	return (int * len(matches))

total_score = 0

for item in range(0, len(left_list)):
	total_score += get_similarity_score(left_list[item], right_list)

print(total_score)
