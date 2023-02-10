def union_and_intersection(list1, list2):
    union = list(set(list1) | set(list2))
    intersection = list(set(list1) & set(list2))
    return union, intersection

list1 = [1, 2, 3, 4, 5]
list2 = [4, 5, 6, 7, 8]
union, intersection = union_and_intersection(list1, list2)
print("Union:", union)
print("Intersection:", intersection)
