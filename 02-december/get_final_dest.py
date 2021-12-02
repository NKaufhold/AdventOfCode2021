input_file = open("test_course.txt")

# Let's try this with a HashMap/Dictionary:
# Key = Direction
# Value = Sum of Number of Steps
my_dict = dict()

for line in input_file:
    wordArray = line.split()

    # Have we already have the current direction stored?
    # If the value hasn't been stored yet, this methode returns NONE
    if not my_dict.get(wordArray[0]):
        my_dict.update({wordArray[0]: int(wordArray[1])})
    else:
        my_dict[wordArray[0]] = my_dict.get(wordArray[0]) + int(wordArray[1])

print(my_dict)

# It is time to get the result:
result = my_dict.get("forward") * (my_dict.get("down")-my_dict.get("up"))
print(result)

input_file.close()
