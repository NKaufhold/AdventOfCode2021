input_file = open('measurement.txt')
# TODO: Only for debug.
#input_file = open("test.txt", "r")
count = 0
prev_val = None

for line in input_file:
    if prev_val and prev_val < line:
        count = count + 1
    #else:
        #print("{} >= {}".format(prev_val, line))
    prev_val = line

print(count)
