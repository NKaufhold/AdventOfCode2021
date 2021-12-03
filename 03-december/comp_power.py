input_file = open("test-report.txt")
#input_file = open("diagnostic-report.txt")

# Count of the numbers:
count_num = None  # No empty report allowed
# Count of the lines:
count_line = 0

# This is counting the numbers:
for line in input_file:
    count_line += 1
    if not count_num:
        count_num = [int(char) for char in line if char != '\n']
    else:
        chars = [int(char) for char in line if char != '\n']
        for i in range(len(count_num)):
            count_num[i] += chars[i]

print(count_num)

# Let's calculate the binary values of the rates:
gamma_rate_bin = [1 if one > (count_line-one) else 0 for one in count_num]
print(gamma_rate_bin)

epsilon_rate_bin = [1 if g == 0 else 0 for g in gamma_rate_bin]
print(epsilon_rate_bin)
