"""Unleashing the Power of Python: Advance Problem solving
1. Given a number N, find sum of all GCDs that can be formed by selecting all the pairs
from 1 to N.
Examples:
Input : 4
Output : 7
Explanation:
Numbers from 1 to 4 are: 1, 2, 3, 4
Result = gcd(1,2) + gcd(1,3) + gcd(1,4) +
gcd(2,3) + gcd(2,4) + gcd(3,4)
= 1 + 1 + 1 + 1 + 2 + 1
= 7
Input : 12
Output : 105
Input : 1
Output : 0
Input : 2
Output : 1"""
print("question 1")
def gcd(a, b):
    if a == 0:
        return b
    return gcd(b % a, a)
def sumOfGCD(n):
    result = 0
    for i in range(1, n + 1):
        for j in range(i + 1, n + 1):
            result += gcd(i, j)
    return result
n = 4
print(sumOfGCD(n))
n = 12
print(sumOfGCD(n))

"""
2. Write a Program that can print a pattern as follows
Example:
Input1 = 'Samarthya'
Input2 = 'Club'
Output = 'SCalmuabrthya'
Explanation:
Result = Input1[0]+Input2[0]+.......+Input1[n-1]+Input2[n-1]
Input1 = 'Python'
Input2 = 'Bootcamp'
Output = 'PByotohtoancmp'
"""
print("\nquestion 2")
def printPattern(s1, s2):
    result = ""
    for i in range(len(s1)+len(s2)):
        try:
            result += s1[i] + s2[i]
        except:
            try:
                result += s1[i]
            except:
                try:
                    result += s2[i]
                except:
                    pass

    print(result)

s1 = "Samarthya"
s2 = "Club"
printPattern(s1, s2)
s1 = "Python"
s2 = "Bootcamp"
printPattern(s1, s2)


"""
3. Write a Program that can print a pattern as follows
Example:
Input = 'Samarthya'
Output = ‘540S1a1m2a3r5t8h13y21a'
Explanation:
len(Input) = 9
fibonacci series for 9 numbers = 0,1,1,2,3,5,8,13,21
Result = sum(fib)+fib(0) + Input[0] + fib(1) + Input[1] + fib(2) + Input[2] + fib(3) +
Input[3] + fib(4) + Input[4] + fib(5) + Input[5] + fib(6) + Input[6] + fib(7) + Input[7] +
fib(8) + Input[8]
= 54 + 0 + 'S' + 1 + 'a' + 1 + 'm' + 2 + 'a' + 3 + 'r' + 5 + 't' + 8 + 'h' + 13 + 'y' + 21 +
'a'
= 540S1a1m2a3r5t8h13y21a
Note:convert int to string using str() function
Input = 'Python'
Output = '200P1y1t2h3o5n8'
"""
print("\nquestion 3")
def fibonacci(n):
    if n < 0:
        print("Incorrect input")
    elif n == 0:
        return 0
    elif n == 1 or n == 2:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

def sumOfFibonacci(n):
    result = 0
    for i in range(n):
        result += fibonacci(i)
    return result
    
def printPattern(s):
    result = ""
    result += str(sumOfFibonacci(len(s)))
    for i in range(len(s)):
        result += str(fibonacci(i)) + s[i]
    result += str(fibonacci(len(s)))
    print(result)
s = "Samarthya"
printPattern(s)
s = "Python"
printPattern(s)



"""
4. Write a Program to remove all the duplicate characters from a string
Example:
Input = 'Ssaamarrthyya'
Output = 'ahmrsty'
Explanation:
Remove all the duplicate characters from the string andd print the string in sorted order
Input = 'Baggage'
Output = 'abeg'
Write a Program to Print diagonal elements of a matrix
Example:
Input = [[1,2,3],[4,5,6],[7,8,9]]
Output = [1,5,9]
Explanation:
Print the diagonal elements of the matrix
Result = [Input[0][0],Input[1][1],Input[2][2]]
Input = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
Output = [1,6,11]
"""
print("\nquestion 4")
def removeDuplicates(s):
    s = list(s)
    s = [i.lower() for i in s]
    s = list(set(s))
    s.sort()
    res = ""
    for i in s:
        res +=i
    return res 
print(removeDuplicates("Ssaamarrthyya"))
print(removeDuplicates("Baggage"))


"""
5. Write a Program to Print the sum of the elements of each row and column of a matrix
Example:
Input = [[1,2,3],[4,5,6],[7,8,9]]
Output = ( [6,15,24] , [12,15,18] )
Explanation:
Print the sum of the elements of each row and column of a matrix
Input = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
Output = ( [10,26,42] , [15,18,21,24] )
"""
print("\nquestion 5")
def printSumOfMatrix(matrix):
    rowSum = []
    colSum = []
    for i in range(len(matrix)):
        rowSum.append(sum(matrix[i]))
    for i in range(len(matrix[0])):
        colSum.append(sum([row[i] for row in matrix]))
    print(rowSum, colSum)
matrix = [[1,2,3],[4,5,6],[7,8,9]]
printSumOfMatrix(matrix)
matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
printSumOfMatrix(matrix)

"""
6. Write a Program to Print the Center column of a matrix
if length of the matrix is odd then print the center column else print the 2nd center
column
Example:
Input = [[1,2,3],[4,5,6],[7,8,9]]
Output = [2,5,8]
Explanation:
Print the center column of the matrix
Input = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
Output = [3,7,11]
"""
print("\nquestion 6")
def printCenterColumn(matrix):
    result = []
    for i in range(len(matrix)):
        result.append(matrix[i][len(matrix[0]) // 2 ])
    print(result)
matrix = [[1,2,3],[4,5,6],[7,8,9]]
printCenterColumn(matrix)
matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
printCenterColumn(matrix)

"""
7. write fizzbuzz program
Example:
Input = 15
Output = [1,2,fizz,4,buzz,fizz,7,8,fizz,buzz,11,fizz,13,14,fizzbuzz]
Explanation:
if number is divisible by 3 print fizz
if number is divisible by 5 print buzz
if number is divisible by 3 and 5 print fizzbuzz
else print the number
Input = 20
Output = [1,2,fizz,4,buzz,fizz,7,8,fizz,buzz,11,fizz,13,14,fizzbuzz,16,17,fizz,19,buzz]
"""
print("\nquestion 7")
def fizzbuzz(n):
    for i in range(1, n+1):
        if i%3==0 and i%5 ==0:
            print("fizzbuzz" , end = " ")
        if i%3 ==0:
            print("fizz", end = " ")
        if i%5 == 0:
            print("buzz",end = " ")
        else:
            print(i,end = " ")
fizzbuzz(15)
print()

"""
8. wirte a program to find the sum of the digits of a in a string
Example:
Input = 'Samarthya'
Output = 106
Explanation:
sum of the digits of the string after converting the string to a number
S = 19 , a = 1 , m = 13 , a = 1 , r = 18 , t = 20 , h = 8 , y = 25 , a = 1
sum of the digits of the string = 19+1+13+1+18+20+8+25+1=106
Input = 'Python'
Output = 98
"""
print("\nquestion 8")
def sumofdigits(string):
    dict ={'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6, 'g': 7, 'h': 8, 'i': 9, 'j': 10, 'k': 11, 'l': 12, 'm': 13, 'n': 14, 'o': 15, 'p': 16, 'q': 17, 'r': 18, 's': 19, 't': 20, 'u': 21, 'v': 22, 'w': 23, 'x': 24, 'y': 25, 'z': 26}
    Sum = 0
    for i in string:
        i = i.lower()
        Sum += dict[i]
    return Sum

print(sumofdigits('Samarthya'))
print(sumofdigits('Python'))


"""
9. Program to find the sum of all numbers present in the string
Example:
Input:abc45def5ghi32
Output:82
Explanation:
The numbers 45, 5 and 32 are present in the string.
Sum = 45 + 5 + 32 = 82.
Input:abc45def5ghi32
Output:82
"""
print("\nquestion 9")
def sum_of_numbers_in_string(string):
    sum = 0
    temp = 0
    for char in string:
        if char.isdigit():
            temp = temp * 10 + int(char)
        else:
            sum += temp
            temp = 0
    sum += temp
    return sum

print(sum_of_numbers_in_string("abc45def5ghi32"))