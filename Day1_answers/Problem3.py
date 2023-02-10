def find_min_max(NumList):
    min = max = NumList[0]
    for i in range(1, len(NumList)):
        if NumList[i] < min:
            min = NumList[i]
        if NumList[i] > max:
            max = NumList[i]
    return min, max

NumList = [1,2,3,5,6]
smallest, largest = find_min_max(NumList)
print("\nThe Smallest Element in this List is : ", smallest)
# print("The Index position of Smallest Element in this List is : ", min_position)
print("\nThe Largest Element in this List is : ", largest)
# print("The Index position of Largest Element in this List is : ", max_position)
