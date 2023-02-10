def palindrome(input_string):
    rev = ""
    for i in input_string:
        rev = i + rev
    return rev == input_string
input_string = "sammas"
if palindrome(input_string):
    print("Yes, It is a palindrome ")
else:
    print("No, It is not a Palindrome")
#Alternative solution
# function which return reverse of a string - GeeksforGeeks solution

# def isPalindrome(s):
# 	return s == s[::-1]


# # Driver code
# s = "malayalam"
# ans = isPalindrome(s)

# if ans:
# 	print("Yes")
# else:
# 	print("No")
