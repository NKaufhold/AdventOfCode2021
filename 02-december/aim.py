#input_file = open("test_course.txt")
input_file = open("real_course.txt")

# Let's try this with a HashMap/Dictionary:
# Key = Direction
# Value = Sum of Number of Steps
my_dict = {"aim": 0, "depth": 0, "horizontal": 0}

for line in input_file:
    wordArray = line.split()

    # Have we already have the current direction stored?
    # If the value hasn't been stored yet, this methode returns NONE
    if wordArray[0] == "down":
        my_dict["aim"] = my_dict.get("aim") + int(wordArray[1])
    elif wordArray[0] == "up":
        my_dict["aim"] = my_dict.get("aim") - int(wordArray[1])
    elif wordArray[0] == "forward":
        my_dict["depth"] = my_dict.get(
            "depth") + (int(wordArray[1]) * my_dict.get("aim"))
        my_dict["horizontal"] = my_dict.get("horizontal") + int(wordArray[1])

    #print(my_dict)

result = my_dict.get("depth") * my_dict.get("horizontal")
print(result)
input_file.close()
