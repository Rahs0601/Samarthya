def sum_and_product(lst):
    result = []
    for tup in lst:
        sum_of_elements = sum(tup)
        product_of_elements = 1
        for element in tup:
            product_of_elements *= element
        result.append((sum_of_elements, product_of_elements))
    return result

lst = [(1, 2, 3), (4, 5, 6), (7, 8, 9)]
result = sum_and_product(lst)
print(result)