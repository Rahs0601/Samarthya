def count_keys(dicts):
    result = {}
    for d in dicts:
        for key in d:
            if key in result:
                result[key] += 1
            else:
                result[key] = 1
    return result

dicts = [{'a': 1, 'b': 2}, {'b': 3, 'c': 4}, {'a': 5, 'c': 6}]
result = count_keys(dicts)
print(result)