def max_frequency(my_string): 
    count = 0
    res = '' 
    for i in my_string: 
        freq = my_string.count(i) 
        if freq > count: 
            count = freq 
            res = i 
    return res

my_string = "Samarthya"
print ("The string is : ")
print(my_string)
my_result = max_frequency(my_string)
print ("The maximum of all characters is : ")
print(my_result)