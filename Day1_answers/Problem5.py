def reverse(input_String):
	str = ""
	for i in input_String:
		str = i + str
	return str

input_String = "Samarthya"

print("The original string is : ", end="")
print(input_String)

print("The reversed string(using loops) is : ", end="")
print(reverse(input_String))