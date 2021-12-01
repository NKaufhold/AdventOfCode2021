input_file = open('measurement.txt')
# TODO: Only for debug.
#input_file = open("test.txt", "r")
count = 0
prev_val = None

for line in input_file:
    value = int(line)
    if prev_val and prev_val < value:
        count = count + 1
    prev_val = value

input_file.close()
print(count)
