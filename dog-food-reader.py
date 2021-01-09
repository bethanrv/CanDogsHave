# dog food reader...
# 	Food
#	- Name
#	- Y/N
#	- Desc

food_list = open("dog-food-list.txt") # open dog foods list file\

formated_list = open("formated-food-list.txt", 'w') # create new file to write in formated data

# save food list into dic
food_list_lines = food_list.readlines()

# save to formated file...
#	myFunc( + name + y/n + desc )
my_func = "addFood";
num = 0
name = ""
status = ""
desc = ""
for line in food_list_lines:
	print(line)
	if(len(line.split(' ')) < 6):
		line = line.strip('\n')
		name = line
	else:
		line = line.strip('\n')
		desc = line
		if(line[0:2] == "No"):
			status = "no"
		else:
			status = "yes"
		food_str = "\"" + name + "\"" +','+ "\"" + status + "\""+','+"\"" + desc + "\""
		print(food_str)
		food_function_str = my_func + "(" + food_str + ");\n"
		print(food_function_str)
		formated_list.write(food_function_str)
	num += 1


# close files
food_list.close()
formated_list.close()

