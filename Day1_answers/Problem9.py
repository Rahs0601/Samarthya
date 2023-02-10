def common(a, b):
	a_set = set(a)
	b_set = set(b)

	if (a_set & b_set):
		print("The common elements from both the list are :"+ str(a_set & b_set))
	else:
		print("No common elements")
		

a = [1, 6, 3, 4, 5]
b = [5, 6, 7, 8, 9]
common(a, b)

# a = input("Enter the first list :").split(' ')
# b = input("Enter the second list :").split(' ')
# common(a, b)