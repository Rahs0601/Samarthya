def MeanMedianMode():
	# Mean
	n = int(input("Enter the number of elements: "))
	n_num = [int(input("Enter the elements: ")) for i in range(n)]
	get_sum = sum(n_num)
	mean = get_sum / n
	print("Mean is: " + str(mean))

	# Median
	n_num.sort()
	if n % 2 == 0:
		median1 = n_num[n//2]
		median2 = n_num[n//2 - 1]
		median = (median1 + median2)/2
	else:
		median = n_num[n//2]
	print("Median is: " + str(median))

	# Mode
	n_num.sort()
	mode = max(set(n_num), key=n_num.count)
	print("Mode is: " + str(mode))


MeanMedianMode()

