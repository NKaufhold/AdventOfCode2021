# Function to calculate the decimal value of a binary number:
def convert(binary_number):
    result = 0
    for i in range(len(binary_number)):
        result += binary_number[i] * 2**(len(binary_number)-1-i)
    return result


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
        # Challenge: Could we do this with only one list comprehension?
        chars = [int(char) for char in line if char != '\n']
        for i in range(len(count_num)):
            count_num[i] += chars[i]


print(count_num)

# Let's calculate the binary values of the rates:
gamma_rate_bin = [1 if one > (count_line-one) else 0 for one in count_num]
print(gamma_rate_bin)
gamma_rate = convert(gamma_rate_bin)
print(gamma_rate)

epsilon_rate_bin = [1 if g == 0 else 0 for g in gamma_rate_bin]
print(epsilon_rate_bin)
epsilon_rate = convert(epsilon_rate_bin)
print(epsilon_rate)
