input_file = open("test.txt", "r")
count = 0

cur_sum = 0
prev_sum = 0

#x = input_file.readlines()[1:4]
#y = map(lambda i: int(i), x)
#print(x)

# my_iter = iter(input_file)
# for (i, line) in zip(my_iter, input_file):
#     print(i, line)

i = 1
for line in input_file:
    cur_sum = sum(map(lambda x: int(x), input_file.readlines()[i:i+3]))

    print(cur_sum)

    # if cur_sum > prev_sum:
    #     count = count + 1
    #
    # prev_sum = cur_sum
    # # DO NOT forget to reset the sum!
    # cur_sum = 0

    i += 1

# print(count)
