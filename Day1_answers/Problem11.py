def removeSpaces(string):

	count = 0

	list = []

	for i in range(len(string)):
		if string[i] != ' ':
			list.append(string[i])

	return toString(list)


def toString(List):
	return ''.join(List)

# Driver program
string = "Rahul Shettigar"
print (removeSpaces(string))
