#input_file = open('measurement.txt')
# TODO: Only for debug.
input_file = open("test.txt", "r")
count = 0

cur_sum = 0
prev_sum = 0

for line in input_file:
    next_line = int(line)
    for i in range(3):
        cur_sum = cur_sum + next_line
        # Is there still a next line?
        if i < 2 and next(input_file):
            next_line = int(next(input_file))
        else:
            cur_sum = -1

    if cur_sum > prev_sum:
        count = count + 1

    prev_sum = cur_sum

print(count)
