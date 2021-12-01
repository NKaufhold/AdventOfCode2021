#input_file = open('measurement.txt')
# TODO: Only for debug.
input_file = open("test.txt", "r")
count = 0
prev_val = None

for line in input_file:
    # Are we looking at the first value?
    if not prev_val:
        prev_val = line
    elif prev_val < line:
        count = count + 1
    prev_val = line

print(count)
