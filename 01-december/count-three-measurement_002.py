input_file = open("test.txt", "r")
lines = map(int, input_file.readlines())
input_file.close

count = 0

cur_sum = 0
prev_sum = 0

num_lines = len(lines)
for i in range(num_lines):
    #print(i)

    if i+2 <= num_lines:
        cur_sum = sum([lines[i], lines[i+1], lines[i+2]])
    else:
        break

    print(i, cur_sum)

    if cur_sum > prev_sum:
        count = count + 1

    prev_sum = cur_sum
    # DO NOT forget to reset the sum!
    cur_sum = 0

print(count)
