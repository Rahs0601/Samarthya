def printFibonacciNumbers(num):

	f1 = 0
	f2 = 1
	if (num < 1):
		return 
	print(f1, end=" ")
	for x in range(1, num):
		print(f2, end=" ")
		next = f1 + f2
		f1 = f2
		f2 = next

num = 5
printFibonacciNumbers(num)



